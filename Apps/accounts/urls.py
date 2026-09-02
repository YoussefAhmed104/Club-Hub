from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('home/', views.test, name='test'),
  path('interests/', views.choose_interests, name='interests'),
  path('login/', views.login_view, name='login'),
  path('signup/', views.register, name='signup'),
  path('verify-email/<uidb64>/<token>/', views.verify_email, name='verify_email'),
  path('logout/', views.user_logout,name='logout'),

  # password reset
  path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/auth/password_reset.html'),name='password_reset'),
  path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/auth/reset_done.html'),name='password_reset_done'),
  path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/auth/reset_confirm.html'),name='password_reset_confirm'),
  path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/auth/reset_complete.html'),name='password_reset_complete'),

  # main pages
  path('all_clubs/', views.all_clubs_view, name='clubs'),
  path('clubs/<int:club_id>/', views.club_details_view, name= 'club_detail'),
  path('clubs/<int:club_id>/members/', views.member_list_view, name= 'members')

]