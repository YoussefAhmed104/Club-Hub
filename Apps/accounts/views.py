from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def test(request):
  return render(request, 'accounts/test.html')


def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      user = authenticate(request, email=email, password=password)

      if user is not None:
        login(request, user)
        return redirect('test')  # Redirect to a success page after login

      form.add_error(None, 'Invalid email or password.')

  else:
    form = LoginForm()

  return render(request, 'accounts/login.html', {'form': form})

def register(request):
  if request.method == 'POST':
    form = RegesterForm(request.POST)

    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password'])
      user.is_active = False
      user.email_verified = False
      user.save()

      uid = urlsafe_base64_encode(force_bytes(user.pk))
      token = default_token_generator.make_token(user)
      verification_url = request.build_absolute_uri(
        reverse('verify_email', kwargs={'uidb64': uid, 'token': token})
      )
      send_mail(
        'Verify your Club Hub account',
        f'Click this link to verify your account: {verification_url}',
        None,
        [user.email],
      )

      return redirect('login')
  else:
    form = RegesterForm()

  return render(request, 'accounts/signup.html', {'form':form})


def verify_email(request, uidb64, token):
  try:
    user_id = force_str(urlsafe_base64_decode(uidb64))
    user = CustomUser.objects.get(pk=user_id)
  except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
    user = None

  if user is None or not default_token_generator.check_token(user, token):
    return HttpResponse('This verification link is invalid or has expired.', status=400)

  user.email_verified = True
  user.is_active = True
  user.save(update_fields=['email_verified', 'is_active'])
  return HttpResponse('Your email has been verified. You can now log in.')


def user_logout(request):
  logout(request)
  messages.success(request,"You are loged out succesfully")
  return redirect('login')