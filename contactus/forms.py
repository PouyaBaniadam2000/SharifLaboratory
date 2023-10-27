from contactus.models import Message
from django import forms


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
