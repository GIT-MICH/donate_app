from django import forms
from portfoliolab_app.models import Account


class LoginForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password', 'password2']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Imię'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email '})
        }
