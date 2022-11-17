from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import ClientModel,ProjectModel

class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Enter  Username : ',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Enter  Password : ',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User()
        fields = ['username','password']

class RegisterForm(UserCreationForm):

    password1 = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

        widgets = {

            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),

        }

class ClientForm(forms.ModelForm):

    class Meta:
        model = ClientModel
        fields = ['client_name']
        labels = {
            'client_name' : 'Enter Client Name ' ,
        }
        widgets = {
            'client_name' : forms.TextInput(attrs={'class':'form-control'}),
        }

class ProjectForm(forms.ModelForm):

    class Meta:
        model = ProjectModel
        fields = ['p_name']
        labels = {
            'p_name' : 'Enter Project Name',
        }
        widgets = {
            'p_name' : forms.TextInput(attrs={'class':'form-control'}),
        }

