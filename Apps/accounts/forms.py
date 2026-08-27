from django import forms
from .models import CustomUser


class LoginForm(forms.Form):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
  password = forms.CharField(widget=forms.PasswordInput)

class RegesterForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput, min_length=8)
  confirm_password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = CustomUser
    fields = [
      'first_name',
      'last_name',
      'nickname',
      'email',
      'school_code',
      'phone_number',
      'grade',
    ]

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')

    if password != confirm_password:
        raise forms.ValidationError("Passwords do not match.")
    
    return cleaned_data