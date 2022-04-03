from django import forms
from .models import Feedback

form_choice=[
        (0,'Rating'),
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
]

from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm


class FooterForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'NAME','class':'footer_newsletter_input'}),label='')
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email','class':'footer_newsletter_input'}),label='')
    phone=forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Phone','class':'footer_newsletter_input'}),label='')
    rating=forms.ChoiceField(widget=forms.Select(attrs={'placeholder':'Rating','class':'footer_newsletter_input'}),label='',choices=form_choice)
    message=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message','class':'footer_newsletter_input'}),label='')
    error_css_class="text-danger"
    class Meta:
        model=Feedback
        fields=['name','email','phone','rating','message']

class FeedbackForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name','class':'input100'}),label='<span class="lnr lnr-user"></span>')
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'EMAIL','class':'input100'}),label='<span class="lnr lnr-envelope"></span>')
    phone=forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'PHONE NUMBER','class':'input100'}),label='<span class="lnr lnr-phone-handset"></span>')
    rating=forms.ChoiceField(widget=forms.Select(attrs={'placeholder':'RATING','class':'input100'}),label='',choices=form_choice)
    message=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'MESSAGE','class':'input100'}),label='')
    class Meta:
        model=Feedback
        fields=['name','email','phone','rating','message']


class CustomPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'Enter your Email ID','class':'input100','autocomplete':'email'}),
        label=" ",
    )

class CustomPasswordResetConfirm(SetPasswordForm):
    new_password1=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Enter New Passoword','class':'input100'}),
        label=" ",
        strip=False
    )
    new_password2=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Enter password again','class':'input100'}),
        label=" ",
        strip=False
    )