from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to="bookmark_images/", blank=True, null=True
    )  # <-- New field

    def __str__(self):
        return self.title
