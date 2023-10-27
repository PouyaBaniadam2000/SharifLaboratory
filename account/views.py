from random import randint
from uuid import uuid4

from account.forms import LoginForm, RegisterForm
from account.mixins import NonAuthenticatedUsersOnlyMixin
from account.models import CustomUser, OTP
from account.sms import send_register_sms
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView


class RegisterView(NonAuthenticatedUsersOnlyMixin, FormView):
    template_name = "account/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("account:check_otp")

    def form_valid(self, form):
        code = randint(1000, 9999)
        receptor = form.cleaned_data.get('phone')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password_1')
        token = str(uuid4())

        send_register_sms(receptor=receptor, code=code)

        OTP.objects.create(phone=receptor, code=code, token=token, username=username, password=password,
                           type="phone_register_mode")

        return redirect(reverse("account:check_otp") + f"?token={token}")

    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):

        mobile_phone_or_username = form.cleaned_data.get('mobile_phone_or_username')
        password = form.cleaned_data.get('password')

        if str(mobile_phone_or_username).isdigit():
            user = CustomUser.objects.get(mobile_phone=mobile_phone_or_username)

        else:
            user = CustomUser.objects.get(username=mobile_phone_or_username)

        authenticated_user = authenticate(self.request, username=user.username, password=password)

        if authenticated_user is not None:
            login(self.request, user)

        else:
            form.add_error('mobile_phone_or_username', 'هیچ حساب کاربری با این مشخصات یافت نشد.')
            return self.form_invalid(form)

        return super().form_valid(form)


class LogOutView(View):
    def get(self, request):
        logout(request)
        next_url = request.GET.get('next', 'home:home')
        return redirect(next_url)
