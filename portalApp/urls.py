
from django.urls import path
from . import views

urlpatterns = [
    path('ProfilePage/', views.ProfilePage,name='ProfilePage'),
    path('EditProfilePage/',views.EditProfilePage,name='EditProfilePage'),
    path('changePasswordPage/',views.changePasswordPage,name='changePasswordPage'),
    #Job Create Section
    path('add_job_Page/',views.add_job_Page,name='add_job_Page'),
    path('viewjobPage/', views.viewjobPage, name='viewjobPage'),
    path('deletePage/<str:myid>',views.deletePage,name='deletePage'),
    path('editPage/<str:myid>',views.editPage,name='editPage'),
    path('updatePage/',views.updatePage,name='updatePage'),
    #Job Apply
    path('applyPage/<str:myid>',views.applyPage,name='applyPage'),
    path('Applied_Job_By_Applicants_Page/',views.Applied_Job_By_Applicants_Page,name='Applied_Job_By_Applicants_Page'),
    #Recruiter See The job applicant
    path('Post_or_Applied_Job_Page/',views.Post_or_Applied_Job_Page,name='Post_or_Applied_Job_Page'),
    path('applicant_list/<str:myid>',views.applicant_list,name='applicant_list'),
]
