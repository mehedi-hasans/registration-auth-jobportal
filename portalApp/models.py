from django.db import models
from authentication.models import Custom_User

# Create your models here.
class RecruiterProfile(models.Model):
    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,null=True, related_name='recruiter_profile')
    
    def __str__(self):
        return self.user.display_name
    
class ApplicantProfile(models.Model):
    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,null=True, related_name='applicant_profile')
    skills=models.CharField(max_length=100,null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    def __str__(self):
        return self.user.display_name
    
#Job Model All
# class job_model(models.Model):
#     DIVISIONS = [
#     ('Dhaka', 'Dhaka Division'),
#     ('CTG', 'Chittagong Division'),
#     ('Khulna', 'Khulna Division'),
#     ('Rajshahi', 'Rajshahi Division'),
#     ('Barishal', 'Barisal Division'),
#     ('Sylhet', 'Sylhet Division'),
#     ('Rangpur', 'Rangpur Division'),
#     ('Mymensingh', 'Mymensingh Division'),
# ]

        
    
#     job_title = models.CharField(max_length=100, null=True)
#     company_name = models.CharField(max_length=100, null=True)
#     Division = models.CharField(choices = DIVISIONS, max_length=100, null=True, default='Dhaka')
    
#     location_Details = models.CharField(max_length=100, null=True)
#     description = models.TextField()
#     job_creator = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
#     create_at = models.DateTimeField(auto_now_add=True, null=True)
#     update_at = models.DateTimeField(auto_now=True, null=True)

#     def __str__(self):
#         return self.job_title    
    
    


class job_model(models.Model):
    job_title = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    job_creator = models.ForeignKey(Custom_User, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title