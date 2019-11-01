from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField(max_length=30)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'from {}'.format(self.name)

