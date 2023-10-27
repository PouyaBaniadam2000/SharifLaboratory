from about.models import About, Faq
from django.views.generic import TemplateView, ListView


class AboutUsView(TemplateView):
    template_name = "about/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_us"] = About.objects.all()
        return context


class FaqView(ListView):
    model = Faq
