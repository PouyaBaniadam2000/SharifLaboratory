from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from project.mixins import IsAllowedMixin
from project.models import Project, Category


class ProjectListView(ListView):
    model = Project
    queryset = Project.objects.filter(is_allowed=True)

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Project.objects.filter(categories__category=category, is_allowed=True)

        return Project.objects.filter(is_allowed=True)


class ProjectDetailView(IsAllowedMixin, DetailView):
    model = Project
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_project = self.object
        next_project = Project.objects.filter(id__gt=current_project.id).order_by('id').first()
        previous_project = Project.objects.filter(id__lt=current_project.id).order_by('-id').first()

        context['next_project'] = next_project
        context['previous_project'] = previous_project

        return context
