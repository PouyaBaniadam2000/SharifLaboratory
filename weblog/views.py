from django.views.generic import ListView, DetailView
from weblog.mixins import IsAllowedMixin
from weblog.models import Weblog, Category
from django.shortcuts import get_object_or_404
from django.utils.encoding import uri_to_iri


class WeblogListView(ListView):
    model = Weblog
    queryset = Weblog.objects.filter(is_allowed=True)

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Weblog.objects.filter(categories__category=category, is_allowed=True)

        return Weblog.objects.filter(is_allowed=True)


class WeblogDetailView(IsAllowedMixin, DetailView):
    model = Weblog
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        slug = uri_to_iri(self.kwargs.get(self.slug_url_kwarg))
        return get_object_or_404(self.model, **{self.slug_field: slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_weblog = self.object
        next_weblog = Weblog.objects.filter(id__gt=current_weblog.id).order_by('id').first()
        previous_weblog = Weblog.objects.filter(id__lt=current_weblog.id).order_by('-id').first()

        context['next_weblog'] = next_weblog
        context['previous_weblog'] = previous_weblog

        return context
