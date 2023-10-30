from django.views.generic import ListView, DetailView
from tiding.mixins import IsAllowedMixin
from tiding.models import Tiding


class TidingListView(ListView):
    model = Tiding
    queryset = Tiding.objects.filter(is_allowed=True)

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Tiding.objects.filter(categories__category=category, is_allowed=True)

        return Tiding.objects.filter(is_allowed=True)


class TidingDetailView(IsAllowedMixin, DetailView):
    model = Tiding
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_tiding = self.object
        next_tiding = Tiding.objects.filter(id__gt=current_tiding.id).order_by('id').first()
        previous_tiding = Tiding.objects.filter(id__lt=current_tiding.id).order_by('-id').first()

        context['next_tiding'] = next_tiding
        context['previous_tiding'] = previous_tiding

        return context
