from django.db.models import Q
from django.shortcuts import render
from django.views import View
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


class SearchView(View):
    template_name = 'home/search_result.html'

    def get(self, request):
        query = request.GET.get('q')

        if not query:
            error_message = "یک عبارت وارد کنید."
            context = {
                'query': query,
                'error_message': error_message,
            }
            return render(request, self.template_name, context)

        weblog_results = Weblog.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
        tiding_results = Tiding.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
        record_results = Record.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
        laboratory_results = Laboratory.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))

        has_weblog_results = weblog_results.exists()
        has_tiding_results = tiding_results.exists()
        has_record_results = record_results.exists()
        has_laboratory_results = laboratory_results.exists()

        has_any_results = (has_weblog_results or has_tiding_results or has_record_results or has_laboratory_results)

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
            'has_any_results': has_any_results,
        }

        return render(request, self.template_name, context)
