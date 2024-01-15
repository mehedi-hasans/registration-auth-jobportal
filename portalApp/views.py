from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import ApplicantProfile, job_model, jobApplyModel
from django.shortcuts import get_object_or_404
from django.contrib.auth import update_session_auth_hash
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
def changePasswordPage(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if check_password(old_password, request.user.password):
            if new_password == confirm_password:
                # Perform your custom logic for changing the password here
                request.user.set_password(new_password)
                request.user.save()

                # Update the user's session to prevent them from being logged out
                update_session_auth_hash(request, request.user)

                messages.success(request, 'Password changed successfully!')
                return redirect('ProfilePage')
            else:
                messages.error(request, 'New Password and Confirm Password do not match.')
        else:
            messages.error(request, 'Old Password is incorrect.')

    return render(request, 'changepassword.html')
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

@login_required
def editPage(request,myid):
    job=job_model.objects.filter(id=myid)
    return render(request,'Recruiter/editJob.html',{'job':job})

@login_required
def updatePage(request):
    user = request.user
    if request.method == 'POST':
        job_id = request.POST.get('jobId')
        job_title = request.POST.get('jobTitle')
        company_name = request.POST.get('companyName')
        location = request.POST.get('location')
        description = request.POST.get('description')
        # Retrieve the existing job instance
        job = get_object_or_404(job_model, id=job_id, job_creator=user)
        # Update the job fields
        job.job_title = job_title
        job.company_name = company_name
        job.location = location
        job.description = description
        # Save the changes
        job.save()
        return redirect("viewjobPage")
    return render(request, 'viewjob.html')

#Applicant
#Apply Job Section
@login_required
def applyPage(request,myid):
    job = get_object_or_404(job_model, id=myid)
    if request.method == 'POST':
        skills = request.POST.get('skills')
        resume = request.FILES.get('resume')
        if skills and resume:
            applicant = request.user
            application = jobApplyModel.objects.create(
                job=job,
                applicant=applicant,
                skills=skills,
                resume=resume,
            )
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect("Applied_Job_By_Applicants_Page")
        else:
            messages.error(request, 'Error in the application form. Please check the fields.')
            
    context={
        'job':job
            }
    return render(request,'Applicant/applyJob.html',context)


def Applied_Job_By_Applicant(request):
    job_seeker=request.user
    applied_job=jobApplyModel.objects.filter(applicant=job_seeker)
    context={
        'applied_job':applied_job, 
    }
    return render(request,'Applicant/AppliedJob.html',context)


#Recruiter
def createdJob_byRecruiter(request):
    current_user=request.user
    if current_user.user_type == 'Recruiter':
        posted_job = job_model.objects.filter(job_creator=current_user)
    context={
        'posted_job':posted_job
    }
    return render(request,'Recruiter/postedJob.html',context)


def applicant_list(request, myid):
    myJob = get_object_or_404(job_model, id=myid)
    applicants = jobApplyModel.objects.filter(job=myJob)
    context = {
        'job': myJob,
        'applicants': applicants,
    }
    return render(request,"Recruiter/applicantList.html",context)


#Search Option
def searchResultsPage(request):
    try:
        query=request.GET.get("search_query")
        if query:
            jobs=job_model.objects.filter(job_title__icontains=query)
        else:
            jobs=[] 
        context={
            'query':query,
            'jobs':jobs,
        }
        return render(request,'Applicant/search_results.html',context)
    except Exception as e:
        return render(request,'Applicant/error.html',{'error_message':str(e)})
