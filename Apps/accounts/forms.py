from django import forms


class LoginForm(forms.Form):
  personal_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
  password = forms.CharField(widget=forms.PasswordInput)