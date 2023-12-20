from django import forms
from allauth.account.forms import SignupForm
from . models import Request
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class CustomSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=255,label='First Name',widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=255,label='Last Name',widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    phone_number = forms.CharField(max_length=255,label='Phone Number',  widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    captcha = ReCaptchaField()

    def save(self, request):
        user = super(CustomSignUpForm,self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user
    

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('description', 'image', 'contact_method')
        widgets = {
            'contact_method': forms.Select(attrs={'class':'form-control'})
        }
        