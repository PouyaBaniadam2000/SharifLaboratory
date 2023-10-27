from home.models import GeneralWebsiteIdea


def footer(request):
    footer_general_website_idea = GeneralWebsiteIdea.objects.last()

    return {'footer_general_website_idea': footer_general_website_idea}
