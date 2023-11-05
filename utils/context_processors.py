from contactus.models import ContactInfo
from home.models import GeneralWebsiteIdea
from laboratory.models import Laboratory


def footer(request):
    footer_general_website_idea = GeneralWebsiteIdea.objects.last()

    return {'footer_general_website_idea': footer_general_website_idea}


# def laboratory_menu(request):
#     laboratory_1 = Laboratory.objects.filter(has_child=True, has_parent=False)
#     laboratory_2 = Laboratory.objects.filter(has_child=True, has_parent=True)
#     laboratory_3 = Laboratory.objects.filter(has_child=False, has_parent=True)
#     return {"laboratory_1": laboratory_1, "laboratory_2": laboratory_2, "laboratory_3": laboratory_3}


def header_menu_info(request):
    contact_us_info = ContactInfo.objects.last()
    return {"contact_us_info": contact_us_info}
