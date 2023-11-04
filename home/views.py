from django.shortcuts import render
from django.views.generic import TemplateView
from home.models import GeneralWebsiteIdea, GeneralWebsiteIdeaImage, SharifLabServicePreview, TeamMember, Certificate
from laboratory.models import Laboratory
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


def search_view(request):
    query = request.GET.get('q')

    if not query:
        error_message = "یک عبارت وارد کنید."
        context = {
            'query': query,
            'error_message': error_message,
        }
        return render(request, 'home/search_result.html', context)

    weblog_results = Weblog.objects.filter(title__icontains=query)
    tiding_results = Tiding.objects.filter(title__icontains=query)
    record_results = Record.objects.filter(title__icontains=query)
    laboratory_results = Laboratory.objects.filter(title__icontains=query)

    has_weblog_results = len(weblog_results) > 0
    has_tiding_results = len(tiding_results) > 0
    has_record_results = len(record_results) > 0
    has_laboratory_results = len(laboratory_results) > 0

    context = {
        'query': query,
        'weblog_results': weblog_results,
        'tiding_results': tiding_results,
        'record_results': record_results,
        'laboratory_results': laboratory_results,
        'has_weblog_results': has_weblog_results,
        'has_tiding_results': has_tiding_results,
        'has_record_results': has_record_results,
        'has_laboratory_results': has_laboratory_results,
    }

    return render(request, 'home/search_result.html', context)