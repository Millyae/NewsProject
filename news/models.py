from django.db import models
from django.utils import timezone
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=255, unique=True, default='')
    content = models.TextField(default='')
    author = models.CharField(max_length=40, unique=False, default='')
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])