
from django.urls import path
from . import views

urlpatterns = [
    path('ProfilePage/', views.ProfilePage,name='ProfilePage'),
    path('EditProfilePage/',views.EditProfilePage,name='EditProfilePage'),

    #Job Create Section
    path('add_job_Page/',views.add_job_Page,name='add_job_Page'),
    path('viewjobPage/', views.viewjobPage, name='viewjobPage'),
    path('deletePage/<str:myid>',views.deletePage,name='deletePage'),
]
