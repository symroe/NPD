from django.db import models
from django.contrib.auth.models import User

class PermissionLevel(models.Model):
    user = models.OneToOneField(User)
    private_access = models.BooleanField(default=False)