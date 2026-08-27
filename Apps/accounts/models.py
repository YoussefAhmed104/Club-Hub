from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import re

class CustomUserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('The Email field must be set')

    user = self.model(email=self.normalize_email(email), **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError("Superuser must have is_staff=True")

    if extra_fields.get('is_superuser') is not True:
      raise ValueError("Superuser must have is_superuser=True")
    return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
  username = None
  GRADE_CHOICES = [
    ('10th', '10th Grade'),
    ('11th', '11th Grade'),
    ('12th', '12th Grade'),
  ]
  nickname = models.CharField(max_length = 50, blank = True, null = True)
  school_email = models.EmailField(unique=True, blank=True, editable=False)
  email = models.EmailField(unique=True)
  school_code = models.CharField(max_length=7 ,unique=True)
  email_verified = models.BooleanField(default=False)
  phone_number = models.CharField(max_length=11)
  profile_img = models.ImageField(upload_to = 'profile_imag/',default = 'profile.png', blank = True, null = True)
  grade = models.CharField(max_length=10, choices = GRADE_CHOICES)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  @property
  def clubs_count(self):
    return Membership.objects.filter(
    user=self,
    is_active=True
    ).count()

  @property
  def full_name(self):
    return f"{self.first_name} {self.last_name}"

  # auto save the school mail
  def save(self, *args, **kwargs):
    clean_name = re.sub(r'\s+', '', self.first_name.strip().lower())
    self.school_email = f"{clean_name}.{self.school_code}@stemoctober.moe.edu.eg"
    super().save(*args, **kwargs)
  
  def __str__(self):
    return self.full_name

class Membership(models.Model):
  ROLE_CHOICES = [
    ('president', 'President'),
    ('vice-president', 'Vice-President'),
    ('mentor', 'Mentor'),
    ('member', 'Member'),
]

  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  club = models.ForeignKey('Club', on_delete=models.CASCADE)
  role = models.CharField(
    max_length=20,
    choices=ROLE_CHOICES,
    default='member'
  )
  joined_at = models.DateField(auto_now_add=True)
  points = models.IntegerField(default=100)
  is_active = models.BooleanField(default=True)


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
    ).count()

  def __str__(self):
    return self.name