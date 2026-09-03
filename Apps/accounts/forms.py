from django import forms
from .models import *


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


class InterestForm(forms.Form):
  interests = forms.ModelMultipleChoiceField(
    queryset= Interests.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    required=True)
  def clean_interests(self):
    interests = self.cleaned_data['interests']

    if len(interests) < 2 :
      raise forms.ValidationError("Please select at least 2 interests")


class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['title', 'description', 'task_link', 'deadline']
    widgets= {
      'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Title'}),
      'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
      'task_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
    }