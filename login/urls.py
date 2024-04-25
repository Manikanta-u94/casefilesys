from django.urls import path
from . import views  

# app_name = "login"

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path("login/login_images/", views.login_images, name="login_images"),
    
]