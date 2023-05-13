from django.contrib.auth.models import User
from django.db import models


class ConfrimCode(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	code = models.CharField(max_length=7)