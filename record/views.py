from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from record.mixins import IsAllowedMixin
from record.models import Record, Category
from django.utils.encoding import uri_to_iri


class RecordListView(ListView):
    model = Record
    queryset = Record.objects.filter(is_allowed=True)

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Record.objects.filter(categories__category=category, is_allowed=True)

        return Record.objects.filter(is_allowed=True)


class RecordDetailView(IsAllowedMixin, DetailView):
    model = Record
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        slug = uri_to_iri(self.kwargs.get(self.slug_url_kwarg))
        return get_object_or_404(self.model, **{self.slug_field: slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_record = self.object
        next_record = Record.objects.filter(id__gt=current_record.id).order_by('id').first()
        previous_record = Record.objects.filter(id__lt=current_record.id).order_by('-id').first()

        context['next_record'] = next_record
        context['previous_record'] = previous_record

        return context
