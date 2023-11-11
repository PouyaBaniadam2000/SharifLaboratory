from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView , View
from laboratory.mixins import IsAllowedMixin
from laboratory.models import Laboratory, Category
from urllib.parse import unquote
from django.core.paginator import Paginator

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


# def laboratory_category_list_view(request, slug):
#     print(slug)
#     category = Category.objects.get(slug=slug)
#     print(category)
#     laboratories = Laboratory.objects.filter(category=category)
#
#     context = {
#         'category': category,
#         'laboratories': laboratories,
#     }
#
#     return render(request, 'laboratory/laboratory_category_list.html', context)


class CategoryDetailView(View):
    """
    View for returning laboratory
    of the selected category
    """

    def get(self, request, slug):
        slug = unquote(slug)
        category = get_object_or_404(Category, slug=slug)
        laboratory = Laboratory.objects.filter(category__title=category)

        # pagination
        page_number = request.GET.get('page')
        paginator = Paginator(laboratory, 15)
        objects_list = paginator.get_page(page_number)

        context = {"laboratories": objects_list, "category": category}
        return render(request, 'laboratory/laboratory_category_list.html', context)