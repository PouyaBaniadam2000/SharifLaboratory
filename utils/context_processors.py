from home.models import GeneralWebsiteIdea
from laboratory.models import Category


def footer(request):
    footer_general_website_idea = GeneralWebsiteIdea.objects.last()

    return {'footer_general_website_idea': footer_general_website_idea}


def category_menu(request):
    category_objects = Category.objects.all()
    return {"category_objects": category_objects}
