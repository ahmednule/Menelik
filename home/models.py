from django.db import models
from django.conf import settings

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=50, null=False)
    password = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Posts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=False )
    image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} {self.created_at}"