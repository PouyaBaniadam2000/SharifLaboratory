from django.shortcuts import redirect
from django.urls import reverse


class NonAuthenticatedUsersOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:home")
        return super(NonAuthenticatedUsersOnlyMixin, self).dispatch(request, *args, **kwargs)


class AuthenticatedUsersOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            redirect_url = reverse("account:login")
            message = "جهت ثبت شکایت، ابتدا باید وارد حساب کاربری خود شوید."
            redirect_url += f'?message={message}'
            return redirect(redirect_url)
        return super(AuthenticatedUsersOnlyMixin, self).dispatch(request, *args, **kwargs)
