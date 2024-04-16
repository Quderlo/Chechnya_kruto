from django.db import models
from django.utils import timezone

from project.settings import AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title