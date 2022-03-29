import uuid

from django.contrib.auth.models import User as us
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user = models.ForeignKey(us, on_delete=models.CASCADE)


class Role(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
