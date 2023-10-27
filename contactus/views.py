from contactus.forms import ContactUsForm
from contactus.models import ContactInfo
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView


class ContactUsView(FormView):
    form_class = ContactUsForm
    template_name = "contactus/contact_us.html"
    success_url = reverse_lazy('contact_us:contact_us')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "پیام شما با موفقیت ارسال شد.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact_info = ContactInfo.objects.last()
        context['contact_info'] = contact_info
        return context
