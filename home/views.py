from django.views.generic import TemplateView
from home.models import GeneralWebsiteIdea, GeneralWebsiteIdeaImage, SharifLabServicePreview, TeamMember, Certificate
from record.models import Record
from tiding.models import Tiding
from weblog.models import Weblog


class Home(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["general_website_idea"] = GeneralWebsiteIdea.objects.last()
        context["general_website_idea_images"] = GeneralWebsiteIdeaImage.objects.all()
        context["sharif_lab_services_previews"] = SharifLabServicePreview.objects.all()
        context["team_members"] = TeamMember.objects.all()
        context["latest_weblogs"] = Weblog.objects.filter(is_allowed=True)[:4]
        context["latest_records"] = Record.objects.filter(is_allowed=True)[:3]
        context["latest_tidings"] = Tiding.objects.filter(is_allowed=True)[:3]
        context["certificates"] = Certificate.objects.all()

        return context
