from contactus.models import Message, Complaint
from django import forms


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ("body",)
