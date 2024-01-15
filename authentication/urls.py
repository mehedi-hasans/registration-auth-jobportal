
from django.urls import path
from authentication.views import signup_f,SignIn,home,logout_f

urlpatterns = [
    path('signup/', signup_f, name="signup"),
    path('login/', SignIn,name="login"),
    path('', home,name="home"),
    path('logout/', logout_f,name="logout"),
]
