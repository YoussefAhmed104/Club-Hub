from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
  ROLE_CHOICES =[
    ('president', 'President'),
    ('vice-president', 'Vice-President'),
    ('mentor', 'Mentor'),
    ('member', 'Member'),
  ]

  GRADE_CHOICES = [
    ('10th', '10th Grade'),
    ('11th', '11th Grade'),
    ('12th', '12th Grade'),
  ]
  nickname = models.CharField(max_length = 50, blank = True, null = True)
  school_code = models.CharField(max_length=7 ,unique=True)
  phone_number = models.CharField(max_length=11)
  profile_img = models.ImageField(upload_to = 'profile_imag/',default = 'profile.png', blank = True, null = True)
  grade = models.CharField(max_length=10, choices = GRADE_CHOICES)
  role = models.CharField(max_length=20, choices =ROLE_CHOICES)
  date_joined = models.DateField(auto_now_add=True)
  
  @property
  def clubs_count(self):
    return Membership.objects.filter(
    user=self,
    is_active=True
    ).count()

  @property
  def full_name(self):
    return f"{self.first_name} {self.last_name}"
  
  def __str__(self):
    return self.full_name

class Membership(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  club = models.ForeignKey('Club', on_delete=models.CASCADE)
  joined_at = models.DateField(auto_now_add=True)
  points = models.IntegerField(default=100)
  is_active = models.BooleanField(default=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['user', 'club'], name='unique_membership')
    ]

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['user', 'club'], name='unique_membership')
    ]

  def __str__(self):
    return f"{self.user.username} - {self.club.name}"

class Club(models.Model):
  name = models.CharField(max_length = 50, unique = True)
  description = models.TextField()
  president = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='president')
  vice_president = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='vice_president')
  mentors = models.ManyToManyField(CustomUser, related_name='mentors')
  members = models.ManyToManyField(CustomUser, through='Membership')
  club_img = models.ImageField(upload_to = 'club_images/', default = 'Club.png')

  @property 
  def members_count(self):
    return Membership.objects.filter(
      club = self,
      is_active=True,
      blank=True,
    ).count()

  def __str__(self):
    return self.name