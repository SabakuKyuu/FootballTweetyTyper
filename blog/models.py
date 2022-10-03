from email.policy import default
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    my_tip = models.CharField(max_length=40, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " użytkonwnika " + str(self.author)
        
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    