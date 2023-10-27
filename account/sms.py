import ghasedakpack as ghasedak


def send_register_sms(receptor, code):
    sms = ghasedak.Ghasedak("ec460cd13f734e63c9cc3dbd58d0fef09fbdbac8f639a1bf26824b87bd88b49e")

    sms_verification = sms.verification(
        {'receptor': receptor, 'type': '1', 'template': 'RedShotRegister', 'param1': code})

    return sms_verification


def send_forget_password_code_sms(receptor, code):
    sms = ghasedak.Ghasedak("ec460cd13f734e63c9cc3dbd58d0fef09fbdbac8f639a1bf26824b87bd88b49e")

    sms_verification = sms.verification(
        {'receptor': receptor, 'type': '1', 'template': 'RedShotForgetPassword', 'param1': code})

    return sms_verification


def send_successfully_uploaded_photos_sms(receptor, name, image_count, photographer):
    sms = ghasedak.Ghasedak("ec460cd13f734e63c9cc3dbd58d0fef09fbdbac8f639a1bf26824b87bd88b49e")

    sms_verification = sms.verification(
        {'receptor': receptor, 'type': '1', 'template': 'RedShotUploadedPhotosSuccessfully', 'param1': name,
         'param2': image_count, 'param3': photographer})

    return sms_verification


def send_raise_shot_price_accepted_sms(receptor, name, each_shot_price):
    sms = ghasedak.Ghasedak("ec460cd13f734e63c9cc3dbd58d0fef09fbdbac8f639a1bf26824b87bd88b49e")

    sms_verification = sms.verification(
        {'receptor': receptor, 'type': '1', 'template': 'RedShotRaiseShotPriceTicketAccepted', 'param1': name,
         'param2': each_shot_price})

    return sms_verification


def send_raise_shot_price_declined_sms(receptor, name, each_shot_price):
    sms = ghasedak.Ghasedak("ec460cd13f734e63c9cc3dbd58d0fef09fbdbac8f639a1bf26824b87bd88b49e")

    sms_verification = sms.verification(
        {'receptor': receptor, 'type': '1', 'template': 'RedShotRaiseShotPriceTicketDeclined', 'param1': name,
         'param2': each_shot_price})

    return sms_verification