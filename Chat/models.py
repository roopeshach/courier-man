from django.db import models

# Create your models here.
from django.contrib.auth.models import User

#chat model betwwen user and admin

class Chat(models.Model):
    user = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user.username)

