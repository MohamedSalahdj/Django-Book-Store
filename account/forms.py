from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class RegisterPublisherForm(UserCreationForm):
    
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     email = forms.EmailField(max_length=50)
#     password = forms.CharField()
#     certificate = forms.FileField(upload_to='certificate/',blank=True,null=True)
    
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password', 'certificate']

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if User.objects.filter(username__iexact=username).exists():
#             raise forms.ValidationError('Username already exists')
#         return username

#     def clean_email(self):
#         email_value = self.cleaned_data['email']
        
#         if User.objects.filter(email=email_value).exists():
#             raise forms.ValidationError('This email already exists')

#         return email_value    
        