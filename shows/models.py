from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q
# Create your models here.

User = settings.AUTH_USER_MODEL


class ShowsGetQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(published__lte=now)

    def search(self, q):
        lookup = (
            Q(title__icontains=q) |
            Q(slug__icontains=q) |
            Q(content__icontains=q) |
            Q(user__username__icontains=q) |
            Q(user__first_name__icontains=q) |
            Q(user__last_name__icontains=q))
        return self.filter(lookup)


class ShowsManager(models.Manager):
    def get_queryset(self):
        return ShowsGetQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, q):
        if q is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(q)


class Shows(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, default=1, blank=True, null=True)
    title = models.CharField(max_length=220)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='image/', blank=True)
    content = models.TextField()
    animation = models.BooleanField()
    published = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = ShowsManager()

    class Meta:
        ordering = ['-published', '-timestamp', '-updated']

    def get_absolute_url(self):
        return f'/shows/{self.slug}'

    def get_update_url(self):
        return f'{self.get_absolute_url()}/edit/'

    def get_delete_url(self):
        return f'{self.get_absolute_url()}/delete/'

    def __str__(self):
        return self.title
