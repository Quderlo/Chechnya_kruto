from django.db import models
from django.utils import timezone

from project.settings import AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title