from django.http import Http404
from django.shortcuts import get_object_or_404
from record.models import Record


class IsAllowedMixin:
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        if slug:
            record = get_object_or_404(Record, slug=slug)

            if not record.is_allowed:
                raise Http404("این پروژه قابل دسترس نمی باشد!")

            return record