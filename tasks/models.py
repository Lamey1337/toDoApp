from django.db import models
from django.utils import timezone

class Task(models.Model):
    description = models.CharField(max_length=200)
    creationDate = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.description


