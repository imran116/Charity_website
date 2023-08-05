from django import forms
from django.contrib.auth.models import User

from donation.models import Newsletter, Contact, Donation, Comment


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


