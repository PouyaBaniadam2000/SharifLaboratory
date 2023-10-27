from django.http import Http404
from django.shortcuts import get_object_or_404
from project.models import Project


class IsAllowedMixin:
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        if slug:
            project = get_object_or_404(Project, slug=slug)

            if not project.is_allowed:
                raise Http404("این پروژه قابل دسترس نمی باشد!")

            return project