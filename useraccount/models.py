from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    # You can add extra fields here later (e.g., avatar, bio)
    pass
