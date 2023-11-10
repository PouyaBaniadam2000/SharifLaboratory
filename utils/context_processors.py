from contactus.models import ContactInfo
from home.models import GeneralWebsiteIdea
from laboratory.models import Laboratory, Category


def footer(request):
    footer_general_website_idea = GeneralWebsiteIdea.objects.last()

    return {'footer_general_website_idea': footer_general_website_idea}


def laboratory_categories(request):
    categories = Category.objects.all()
    return {"categories": categories}


def header_menu_info(request):
    contact_us_info = ContactInfo.objects.last()
    return {"contact_us_info": contact_us_info}
