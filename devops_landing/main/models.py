from django.db import models
from django.core.cache import cache

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete('all_projects')  # Remove cache via save

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        cache.delete('all_projects')  # Remove cache via delete

    def __str__(self):
        return self.title