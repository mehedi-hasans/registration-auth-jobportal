from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import ApplicantProfile, job_model
# Create your views here.
@login_required
def ProfilePage(request):
    user=request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)

@login_required
def EditProfilePage(request):
    context = {
        'password_not_matched': "Password Not Matched",
        'Success_Message': "Update Successfully"
    }
    user = request.user
    # Check if the user is authenticated
    if not user.is_authenticated:
        # Redirect or handle the situation appropriately
        return redirect('loginPage')
    
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        display_name = request.POST.get("display_name")
        about = request.POST.get("about")
        image = request.FILES.get("image")

        skills = request.POST.get("skills")
        resume = request.FILES.get("resume")
        
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")


        if password != confirm_password:
            messages.error(request, 'Password and Confirm Password Not Match')
            return redirect('EditProfilePage')
        
        if not check_password(password, user.password):
            messages.error(request, 'Wrong Password')
            return redirect('EditProfilePage')

        user.first_name = first_name
        user.last_name = last_name
        user.display_name = display_name
        user.about = about

        if user.user_type == 'Applicant':
            applicant_profile, created = ApplicantProfile.objects.get_or_create(user=user)
            applicant_profile.skills = skills
            applicant_profile.resume = resume
            applicant_profile.save()

        # Update profile picture if provided
        if image:
            user.profile_image = image
        user.save()

        messages.success(request, "Update Successfully")
        return redirect('ProfilePage')
    return render(request, 'EditProfile.html', context)





#Add Job Create Section
@login_required
def add_job_Page(request):
    user = request.user
    if request.method == 'POST':
        jobTitle=request.POST.get('jobTitle')
        companyName=request.POST.get('companyName')
        location=request.POST.get('location')
        description=request.POST.get('description')

        job=job_model(
            job_title=jobTitle,
            company_name=companyName,
            location=location,
            description=description,
            job_creator=user,
        )
        job.save()
        return redirect("viewjobPage")
    return render(request,'Recruiter/AddJob.html')


def viewjobPage(request):
    job=job_model.objects.all()
    context={
        'jobs':job
    }
    return render(request,"viewjob.html",context)

@login_required
def deletePage(request, myid):
    job=job_model.objects.filter(id=myid)
    job.delete()
    return redirect("viewjobPage")