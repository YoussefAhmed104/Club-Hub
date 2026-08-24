from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def test(request):
  return render(request, 'accounts/test.html')


def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      personal_email = form.cleaned_data['personal_email']
      password = form.cleaned_data['password']
      user = authenticate(request, personal_email=personal_email, password=password)

      if user is not None:
        login(request, user)
        return redirect('test')  # Redirect to a success page after login

      form.add_error(None, 'Invalid email or password.')

  else:
    form = LoginForm()

  return render(request, 'accounts/login.html', {'form': form})