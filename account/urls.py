from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogOutView.as_view(), name="logout"),
    path("otp/check", views.CheckOTPView.as_view(), name="check_otp"),
    path("password/forget", views.ForgetPassword.as_view(), name="forget_password"),
    path("password/change", views.ChangePassword.as_view(), name="change_password"),
]
