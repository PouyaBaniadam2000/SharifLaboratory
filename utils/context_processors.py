from contactus.models import ContactInfo
from home.models import GeneralWebsiteIdea
from laboratory.models import Category


def footer(request):
    footer_general_website_idea = GeneralWebsiteIdea.objects.last()

    return {'footer_general_website_idea': footer_general_website_idea}


def category_menu(request):
    category_objects = Category.objects.all()
    return {"category_objects": category_objects}


def header_menu_info(request):
    contact_us_info = ContactInfo.objects.last()
    return {"contact_us_info": contact_us_info}
