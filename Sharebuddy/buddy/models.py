
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class User(AbstractUser):
    pass

