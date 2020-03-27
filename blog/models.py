from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):
    groupname = models.CharField(max_length=50)
    topic = models.TextField()
    member1=models.CharField(max_length=50)
    member2=models.CharField(max_length=50)
    member3=models.CharField(max_length=50)
    member4=models.CharField(max_length=50)
    guidename=models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.groupname
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()    
