from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from admission.forms import AdmissionForm


class AdmissionView(FormView):
    form_class = AdmissionForm
    template_name = "admission/admission_form.html"
    success_url = reverse_lazy("admission:form")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "فرم پذیرش شما با موفقیت ثبت شد.")
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
