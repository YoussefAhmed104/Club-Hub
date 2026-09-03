from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count , Q

@login_required(login_url='login')
def test(request):
  clubs = Club.objects.filter(interests__in=request.user.interests.all()).distinct()
  return render(request, 'accounts/test.html', {"clubs": clubs})


def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      user = authenticate(request, email=email, password=password)

      if user is not None:
        login(request, user)

        if len(request.user.interests.all()) == 0:
          return redirect('interests')
        else:
          return redirect('test')

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


@login_required
def choose_interests(request):
  if request.method =="POST":
    form = InterestForm(request.POST)

    if form.is_valid():
      request.user.interests.set(form.cleaned_data["interests"])
      return redirect("test")
      
    else:
      print("forms errors:", form.errors)
  else:
    form = InterestForm()

  return render(request, "interests.html", {"form":form})

@login_required
def recommended_clubs_view(request):
  user_interests = request.user.userprofile.interests.all()

  recommended_clubs = (
    Club.objects.filter(Interests__in = user_interests).annotate(
      count = Count('interests', filter=Q(Interests__in = user_interests))
    )
    .distinct().order_by('-count')
  )
  return render(request, 'interests.html', {'recommended_clubs': recommended_clubs})

@login_required
def all_clubs_view(request):
  clubs = Club.objects.all()
  return render(request, 'pages/all_clubs.html', {'clubs':clubs})

@login_required
def club_details_view(request, club_id):
  club = get_object_or_404(Club, pk= club_id)

  return render(request, 'pages/club_details.html', {'club': club})

@login_required
def member_list_view(request, club_id):
  club = get_object_or_404(Club, pk= club_id)
  memberships = Membership.objects.filter(
    club=club, is_active=True
  ).select_related('user').order_by('points', 'user__first_name')

  return render(request, 'pages/members_list.html', {'club': club, 'memberships': memberships})


@login_required
def tastks(request, club_id):
  club = get_object_or_404(Club, pk= club_id)
  tasks = Task.objects.filter(club=club).order_by('deadline')

  return render(request, 'pages/club_task.html', {'club':club, 'tasks':tasks})


@login_required
def add_task_view(request, club_id):
  club = get_object_or_404(Club, pk= club_id)
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      task = form.save(commit=False)
      task.club= club
      task.created_by = request.user
      task.save()
      return redirect('club_task', club_id=club.id)
  else:
    form = TaskForm()

  return render(request, 'pages/add_task.html', {'club':club, 'form':form})

