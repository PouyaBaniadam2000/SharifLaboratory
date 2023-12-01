from random import randint
from uuid import uuid4

from django.http import HttpResponseRedirect

from account.forms import LoginForm, RegisterForm, CheckOTPForm, ChangePasswordForm, ForgetPasswordForm
from account.mixins import NonAuthenticatedUsersOnlyMixin
from account.models import CustomUser, OTP
from account.sms import send_register_sms, send_forget_password_code_sms
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView


class RegisterView(NonAuthenticatedUsersOnlyMixin, FormView):
    template_name = "account/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        code = randint(1000, 9999)
        receptor = form.cleaned_data.get('mobile_phone')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        landline_phone = form.cleaned_data.get('landline_phone')
        postal_code = form.cleaned_data.get('postal_code')
        address = form.cleaned_data.get('address')
        company_name = form.cleaned_data.get('company_name')
        activity_field = form.cleaned_data.get('activity_field')
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        token = str(uuid4())

        # send_register_sms(receptor=receptor, code=code)
        print(code)

        OTP.objects.create(mobile_phone=receptor, code=code, token=token, landline_phone=landline_phone,
                           postal_code=postal_code, address=address, company_name=company_name,
                           activity_field=activity_field, email=email, first_name=first_name, last_name=last_name,
                           username=username, password=password, type="phone_register_mode")

        return redirect(reverse("account:check_otp") + f"?token={token}")

    def form_invalid(self, form):
        return super().form_invalid(form)


class CheckOTPView(FormView):
    form_class = CheckOTPForm
    template_name = 'account/check_otp_code.html'

    def form_valid(self, form):
        token = self.request.GET.get('token')
        if OTP.objects.filter(token=token, code=form.cleaned_data.get('code'), type="phone_register_mode").exists():
            otp = OTP.objects.get(token=token)

            user = CustomUser.objects.create_user(mobile_phone=otp.mobile_phone, landline_phone=otp.landline_phone,
                                                  username=otp.username, password=otp.password, email=otp.email,
                                                  first_name=otp.first_name, last_name=otp.last_name,
                                                  postal_code=otp.postal_code, address=otp.address,
                                                  company_name=otp.company_name, activity_field=otp.activity_field)

            login(self.request, user)
            otp.delete()
            otp.save()

            success_url = reverse_lazy('home:home')
            return HttpResponseRedirect(success_url)

        elif OTP.objects.filter(token=token, code=form.cleaned_data.get('code'), type="forget_password_mode").exists():
            return redirect(reverse("account:change_password") + f"?token={token}")

        elif OTP.objects.filter(token=token, code=form.cleaned_data.get('code'), type="delete_account_mode").exists():
            otp = OTP.objects.get(token=token)
            user_to_be_deleted = CustomUser.objects.get(username=otp.username, phone=otp.phone, city=otp.city)

            user_to_be_deleted.delete()
            return redirect("home:home")

        else:
            form.add_error('code', 'کد تأیید نامعتبر است یا منقضی شده است.')
            return self.form_invalid(form)


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


class ForgetPassword(NonAuthenticatedUsersOnlyMixin, FormView):
    template_name = "account/forget_password.html"
    form_class = ForgetPasswordForm
    success_url = reverse_lazy("account:check_otp")

    def form_valid(self, form):
        mobile_phone_or_username = form.cleaned_data.get('mobile_phone_or_username')

        if str(mobile_phone_or_username).isdigit():
            user = CustomUser.objects.get(mobile_phone=mobile_phone_or_username)

        else:
            user = CustomUser.objects.get(username=mobile_phone_or_username)

        receptor = user.mobile_phone

        code = randint(1000, 9999)
        token = str(uuid4())

        # send_forget_password_code_sms(receptor=receptor, code=code)
        print(code)

        OTP.objects.create(mobile_phone=receptor, code=code, token=token, type="forget_password_mode")
        receptor = f"{receptor[7:12]}...{receptor[0:4]}"
        return redirect(reverse("account:check_otp") + f"?token={token}&mobile_phone={receptor}")

    def form_invalid(self, form):
        return super().form_invalid(form)


class ChangePassword(NonAuthenticatedUsersOnlyMixin, FormView):
    form_class = ChangePasswordForm
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        new_password = form.cleaned_data.get('password_1')
        token = self.request.GET.get('token')

        retrieved_user = OTP.objects.get(token=token)

        username = CustomUser.objects.get(mobile_phone=retrieved_user)
        user = CustomUser.objects.get(username=username)

        user.set_password(new_password)
        user.save()

        login(self.request, user)

        try:
            retrieved_user.delete()
        except:
            pass

        return redirect(reverse("home:home"))
