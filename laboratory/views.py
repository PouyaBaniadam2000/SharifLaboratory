from django.views.generic import DetailView, ListView

from laboratory.models import Category, Laboratory


class AllLaboratory(ListView):
    model = Laboratory


class LaboratoryDetail(DetailView):
    model = Laboratory


class CategoryLaboratoryListView(ListView):
    model = Category
    template_name = 'laboratory/laboratory_list.html'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(pk=category_id)
        return Laboratory.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context['category'] = Category.objects.get(pk=category_id)
        return context
