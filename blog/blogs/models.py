from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    context = models.TextField()
    date_added = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_added']
