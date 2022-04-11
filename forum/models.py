from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Subforum(models.Model):
    parent = models.ForeignKey("Subforum", on_delete=models.CASCADE, default=None, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default=None, blank=True, null=True)
    icon = models.ImageField(upload_to='subforum_icons', default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Thread(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subforum = models.ForeignKey(Subforum, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        print("dupa")
        return reverse('thread-detail', kwargs={'pk': self.id})

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username + " w temacie \"" + self.thread.title + "\": " + self.content

    def get_absolute_url(self):
        return reverse('thread-detail', kwargs={'pk': self.thread.id})