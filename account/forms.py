import string

from django import forms
from django.core.exceptions import ValidationError

from account.models import CustomUser

allowed_characters = []
for _ in string.ascii_letters:
    allowed_characters.append(_)
for __ in range(0, 10):
    allowed_characters.append(str(__))
allowed_characters.append("_")
allowed_characters.append("-")


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_repeat = forms.CharField(widget=forms.PasswordInput, label='تکرار رمز عبور')

    class Meta:
        model = CustomUser
        fields = "__all__"

    def clean_mobile_phone(self):
        print('vfe')
        mobile_phone = self.cleaned_data.get("mobile_phone")
        mobile_phone_exists = True

        try:
            CustomUser.objects.get(mobile_phone=mobile_phone)
        except:
            mobile_phone_exists = False

        if mobile_phone_exists:
            raise ValidationError("کاربر با این شماره تلفن همراه از قبل موجود است.",
                                  code="already registered mobile_phone")

        if not str(mobile_phone).isnumeric():
            raise ValidationError("شماره تلفن همراه فقط میتواند از ارقام تشکیل شده باشد.", code="11 digits only")

        if len(str(mobile_phone)) != 11:
            raise ValidationError("شماره تلفن همراه فقط میتواند فقط 11 رقم داشته باشد.", code="11 digits only")

        if str(mobile_phone)[0] != "0" or str(mobile_phone[1]) != "9":
            raise ValidationError("شماره تلفن همراه نامعتبر است.",
                                  code="starts with zero at first and another digit but zero from the second digit")

        if len(set(mobile_phone)) < 3:
            raise forms.ValidationError("شماره تلفن همراه نامعتبر است.", code="all the same digit")

        return mobile_phone

    def clean_username(self):
        username = str(self.cleaned_data.get("username")).lower()
        username_exists = True

        try:
            CustomUser.objects.get(username=username)
        except:
            username_exists = False

        if username_exists:
            raise ValidationError("کاربر با این نام کاربری از قبل موجود است.", code="already registered mobile_phone")

        if len(str(username)) < 2:
            raise ValidationError("نام کاربری باید حداقل 2 کاراکتر داشته باشد.")

        if str(username).isnumeric():
            raise ValidationError("نام کاربری باید حداقل 1 حرف انگلیسی داشته باشد.")

        for character_checker in username:
            if character_checker not in allowed_characters:
                raise ValidationError("فرمت وارد شده صحیح نیست. (فقط حروف انگلیسی، ارقام، '-'و '_')")

        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")

        if password and password_repeat and password != password_repeat:
            raise forms.ValidationError("پسورد ها با یکدیگر همخوانی ندارند!")


class CheckOTPForm(forms.Form):
    code = forms.CharField(max_length=4, widget=forms.TextInput(
        attrs={'pattern': '[0-9]*', 'oninput': 'this.value = this.value.replace(/[^0-9]/g, "")'}), label="کد")


class ForgetPasswordForm(forms.Form):
    mobile_phone_or_username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={}),
                                               label="شماره تلفن همراه یا نام کاربری")

    def clean_mobile_phone_or_username(self):
        mobile_phone_or_username = self.cleaned_data.get("mobile_phone_or_username")

        mobile_phone = ""
        username = ""

        if str(mobile_phone_or_username).isdigit():
            mobile_phone = mobile_phone_or_username

        else:
            username = mobile_phone_or_username

        if mobile_phone:
            mobile_phone_exists = True
            try:
                CustomUser.objects.get(mobile_phone=mobile_phone)
            except:
                mobile_phone_exists = False

            if not mobile_phone_exists:
                raise ValidationError("کاربری با این شماره تلفن همراه یافت نشد.", code="not registered mobile_phone")

            if not str(mobile_phone).isnumeric():
                raise ValidationError("شماره تلفن همراه فقط میتواند از ارقام تشکیل شده باشد.", code="11 digits only")

            if len(str(mobile_phone)) != 11:
                raise ValidationError("شماره تلفن همراه فقط میتواند فقط 11 رقم داشته باشد.", code="11 digits only")

            if str(mobile_phone)[0] != "0" or str(mobile_phone[1]) != "9":
                raise ValidationError("شماره تلفن همراه نامعتبر است.", code="invalid mobile_phone")

            if len(set(mobile_phone)) < 3:
                raise forms.ValidationError("شماره تلفن همراه نامعتبر است.", code="all the same digit")

        else:
            username_exists = True

            try:
                CustomUser.objects.get(username=username)
            except:
                username_exists = False

            if not username_exists:
                raise ValidationError("کاربری با این نام کاربری یافت نشد.", code="already registered mobile_phone")

            if len(str(username)) < 2:
                raise ValidationError("نام کاربری باید حداقل 2 کاراکتر داشته باشد.")

            if str(username).isnumeric():
                raise ValidationError("نام کاربری باید حداقل 1 حرف انگلیسی داشته باشد.")

            for character_checker in username:
                if character_checker not in allowed_characters:
                    raise ValidationError("فرمت وارد شده صحیح نیست. (فقط حروف، ارقام، '-'و '_'")

        return mobile_phone_or_username

    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data.get("mobile_phone")
        mobile_phone_exists = True

        try:
            CustomUser.objects.get(mobile_phone=mobile_phone)
        except:
            mobile_phone_exists = False

        if not mobile_phone_exists:
            raise ValidationError("کاربری با این شماره یافت نشد.", code="not registered mobile_phone")

        if not str(mobile_phone).isnumeric():
            raise ValidationError("شماره تلفن همراه فقط میتواند از ارقام تشکیل شده باشد.", code="11 digits only")

        if len(str(mobile_phone)) != 11:
            raise ValidationError("شماره تلفن همراه فقط میتواند فقط 11 رقم داشته باشد.", code="11 digits only")

        if str(mobile_phone)[0] != "0" or str(mobile_phone[1]) != "9":
            raise ValidationError("شماره تلفن همراه نامعتبر است.", code="invalid mobile_phone")

        if len(set(mobile_phone)) < 3:
            raise forms.ValidationError("شماره تلفن همراه نامعتبر است.", code="all the same digit")

        return mobile_phone


class ChangePasswordForm(forms.Form):
    password_1 = forms.CharField(
        widget=forms.PasswordInput(attrs={}), label="رمز عبور")

    password_2 = forms.CharField(
        widget=forms.PasswordInput(attrs={}), label="تکرار رمز عبور")

    def clean(self):
        password_1 = self.cleaned_data.get("password_1")
        password_2 = self.cleaned_data.get("password_2")

        if len(password_1) < 4:
            raise ValidationError("رمز عبور باید حداقل 4 کاراکتر داشته باشد.", code="at least 4 characters")

        # if str(password_1).isnumeric():
        #     raise ValidationError("رمز عبور باید باید حداقل 1 حرف انگلیسی داشته باشد.", code="at least 1 letter")
        #
        # if str(password_1).isdigit():
        #     raise ValidationError("رمز عبور باید باید حداقل 1 عدد داشته باشد.", code="at least 1 digit")

        if password_1 != password_2:
            raise ValidationError("رمز عبور های وارد شده، مشابه نیستند.", code="passwords dis-match")


class LoginForm(forms.Form):
    mobile_phone_or_username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={}), label="شماره تلفن همراه یا نام کاربری")

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={}), label="رمز عبور")

    def clean(self):
        mobile_phone_or_username = self.cleaned_data.get("mobile_phone_or_username")

        mobile_phone = ""
        username = ""

        if str(mobile_phone_or_username).isdigit():
            mobile_phone = mobile_phone_or_username

        else:
            username = mobile_phone_or_username

        if mobile_phone:
            mobile_phone_exists = True
            try:
                CustomUser.objects.get(mobile_phone=mobile_phone)
            except:
                mobile_phone_exists = False

            if not mobile_phone_exists:
                raise ValidationError("کاربری با این شماره یافت نشد.", code="not registered mobile_phone")

            if not str(mobile_phone).isnumeric():
                raise ValidationError("شماره تلفن همراه فقط میتواند از ارقام تشکیل شده باشد.", code="11 digits only")

            if len(str(mobile_phone)) != 11:
                raise ValidationError("شماره تلفن همراه فقط میتواند فقط 11 رقم داشته باشد.", code="11 digits only")

            if str(mobile_phone)[0] != "0" or str(mobile_phone[1]) != "9":
                raise ValidationError("شماره تلفن همراه نامعتبر است.", code="invalid mobile_phone")

            if len(set(mobile_phone)) < 3:
                raise forms.ValidationError("شماره تلفن همراه نامعتبر است.", code="all the same digit")

        else:
            username_exists = True

            try:
                CustomUser.objects.get(username=username)
            except:
                username_exists = False

            if not username_exists:
                raise ValidationError("کاربری با این نام کاربری یافت نشد.", code="already registered username")

            if len(str(username)) < 2:
                raise ValidationError("نام کاربری باید حداقل 2 کاراکتر داشته باشد.")

            if str(username).isnumeric():
                raise ValidationError("نام کاربری باید حداقل 1 حرف انگلیسی داشته باشد.")

            for character_checker in username:
                if character_checker not in allowed_characters:
                    raise ValidationError("فرمت وارد شده صحیح نیست. (فقط حروف، ارقام، '-'و '_'")
