from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    # Honeypot field (hidden in HTML)
    website = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website:
            raise forms.ValidationError("Bot detected.")
        return website