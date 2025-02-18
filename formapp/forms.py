from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    phone = forms.CharField(max_length=15, label='Your Phone')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')