from django.http import Http404
from django.shortcuts import get_object_or_404
from tiding.models import Tiding


class IsAllowedMixin:
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        if slug:
            tiding = get_object_or_404(Tiding, slug=slug)

            if not tiding.is_allowed:
                raise Http404("این خبر قابل دسترس نمی باشد!")

            return tiding