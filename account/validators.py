import string

from django.core.exceptions import ValidationError

import account.models

allowed_characters_for_username = []
for _ in string.ascii_letters:
    allowed_characters_for_username.append(_)
for __ in range(0, 10):
    allowed_characters_for_username.append(str(__))
allowed_characters_for_username.append("_")
allowed_characters_for_username.append("-")

not_starting_and_finishing_with_for_username = ["_", "-"]


def is_single_language(name):
    english_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    persian_chars = set("آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی")

    has_english_chars = any(char in english_chars for char in name)
    has_persian_chars = any(char in persian_chars for char in name)

    return has_english_chars != has_persian_chars


def has_digits(value):
    for digit in range(1, 10):
        if str(digit) in value:
            return True
    return False


def validate_username(value):
    username = str(value).lower()

    try:
        user = account.models.CustomUser.objects.get(username=username)
        if user.username != value:
            raise ValidationError("کاربر با این نام کاربری از قبل موجود است.")

    except account.models.CustomUser.DoesNotExist:
        pass

    if str(username).isnumeric():
        raise ValidationError("نام کاربری باید حداقل 1 حرف انگلیسی داشته باشد.")

    if str(username)[0] in not_starting_and_finishing_with_for_username:
        raise ValidationError(f"نام کاربری نمیتواند با ({username[0]}) شروع شود.")

    if str(username)[-1] in not_starting_and_finishing_with_for_username:
        raise ValidationError(f"نام کاربری نمیتواند با ({username[-1]}) تمام شود.")

    if len(str(username)) < 2:
        raise ValidationError("نام کاربری باید حداقل 2 کاراکتر داشته باشد.")

    for character_checker in username:
        if character_checker not in allowed_characters_for_username:
            raise ValidationError("فرمت وارد شده صحیح نیست. (فقط حروف انگلیسی، ارقام، '-'و '_')")

    if not any(c.isalpha() for c in username):
        raise ValidationError("نام کاربری باید حداقل 1 حرف انگلیسی داشته باشد.")


def validate_mobile_phone(value):
    if not str(value).isnumeric():
        raise ValidationError("شماره تلفن فقط میتواند از ارقام تشکیل شده باشد.", code="digits only")
    if len(value) != 11:
        raise ValidationError(f"شماره تلفن فقط میتواند 11 رفم داشته باشد. ({len(str(value))} رقم دارد.)",
                              code="11 digits only")
    if value[0] != "0":
        raise ValidationError("شماره تلفن نامعتبر است.")


def validate_landline_phone(value):
    if not str(value).isnumeric():
        raise ValidationError("شماره تلفن ثابت فقط میتواند از ارقام تشکیل شده باشد.", code="digits only")
    if value[0] != "0":
        raise ValidationError("شماره تلفن نامعتبر است.")


def validate_email(value):
    email = value
    email_exists = True

    try:
        user = (account.models.CustomUser.objects.get(email=email))
        if user.email == value:
            email_exists = False
    except account.models.CustomUser.DoesNotExist:
        email_exists = False

    if email_exists:
        raise ValidationError("کاربر با این ایمیل از قبل موجود است.", code="already registered email")


def validate_first_name(value):
    if not value.isalpha():
        if " " in value:
            raise ValidationError("نام نمیتواند فاصله داشته باشد.", code="no space allowed")
        else:
            raise ValidationError("نام فقط میتواند از حروف تشکیل شود.", code="just letters")

    if len(value) < 2:
        raise ValidationError("نام باید حداقل 2 کاراکتر داشته باشد.", code="more than 2 chars")

    if has_digits(value):
        raise ValidationError("نام نمیتواند شامل ارقام باشد.", code="no digits")

    if is_single_language(value):
        pass
    else:
        raise ValidationError("نام فقط میتواند از یک زبان تشکیل شود. (یا انگلیسی یا فارسی)", code="just 1 language")


def validate_last_name(value):
    if not value.isalpha():
        if " " in value:
            pass
        else:
            raise ValidationError("نام خانوادگی فقط میتواند از حروف تشکیل شود.", code="just letters")

    if len(value) < 3:
        raise ValidationError("نام خانوادگی باید حداقل 3 کاراکتر داشته باشد.", code="more than 3 chars")

    if has_digits(value):
        raise ValidationError("نام خانوادگی نمیتواند شامل ارقام باشد.", code="no digits")

    if is_single_language(value):
        pass
    else:
        raise ValidationError("نام خانوادگی فقط میتواند از یک تشکیل ساخته شود. (یا انگلیسی یا فارسی)",
                              code="just 1 language")
