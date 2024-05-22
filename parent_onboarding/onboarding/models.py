from django.db import models

class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)
    parent_type = models.CharField(max_length=20, choices=[('first-time', 'First-Time'), ('experienced', 'Experienced')])
    preferences = models.JSONField(default=dict)  # JSONField

    def __str__(self):
        return self.name

class Child(models.Model):
    user = models.ForeignKey(User, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('unisex', 'Unisex')])

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    age_group = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('unisex', 'Unisex')], null=True)
    content_type = models.CharField(max_length=10, choices=[('blog', 'Blog'), ('vlog', 'Vlog')])
    url = models.URLField(null=True, blank=True)


# Create your models here.
