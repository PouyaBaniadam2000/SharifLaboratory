from django.http import Http404
from django.shortcuts import get_object_or_404
from laboratory.models import Laboratory


class IsAllowedMixin:
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        if slug:
            laboratory = get_object_or_404(Laboratory, slug=slug)

            if not laboratory.is_allowed:
                raise Http404("این آزمایشگاه قابل دسترس نمی باشد!")

            return laboratory