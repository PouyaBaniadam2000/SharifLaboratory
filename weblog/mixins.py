from django.http import Http404
from django.shortcuts import get_object_or_404
from weblog.models import Weblog


class IsAllowedMixin:
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        if slug:
            weblog = get_object_or_404(Weblog, slug=slug)

            if not weblog.is_allowed:
                raise Http404("این وبلاگ قابل دسترس نمی باشد!")

            return weblog