from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class User(AbstractUser):
    pass

    class meta:
        unique_together = ('username', 'email')
