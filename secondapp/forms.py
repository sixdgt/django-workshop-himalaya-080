from django import forms
from secondapp.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "email", "phone_no", "address", "message")