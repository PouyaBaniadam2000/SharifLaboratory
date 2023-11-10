from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView
from laboratory.mixins import IsAllowedMixin
from laboratory.models import Laboratory, Category


class LaboratoryListView(ListView):
    model = Laboratory
    queryset = Laboratory.objects.filter(is_allowed=True)

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Laboratory.objects.filter(categories__category=category, is_allowed=True)

        return Laboratory.objects.filter(is_allowed=True)


class LaboratoryDetailView(IsAllowedMixin, DetailView):
    model = Laboratory
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_laboratory = self.object
        next_laboratory = Laboratory.objects.filter(id__gt=current_laboratory.id).order_by('id').first()
        previous_laboratory = Laboratory.objects.filter(id__lt=current_laboratory.id).order_by('-id').first()

        context['next_laboratory'] = next_laboratory
        context['previous_laboratory'] = previous_laboratory

        return context


def laboratory_category_list_view(request, slug):
    print(slug)
    category = Category.objects.get(slug=slug)
    print(category)
    laboratories = Laboratory.objects.filter(category=category)

    context = {
        'category': category,
        'laboratories': laboratories,
    }

    return render(request, 'laboratory/laboratory_category_list.html', context)
