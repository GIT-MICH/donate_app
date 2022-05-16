from django import forms
from portfoliolab_app.models import Account


class LoginForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Imię'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Hasło'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email '})
        }
