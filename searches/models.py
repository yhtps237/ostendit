from django.db import models
from django.conf import settings
# Create your models here.


class Search(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)
    query = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
