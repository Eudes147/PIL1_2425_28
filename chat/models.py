from django.db import models
from django.contrib.auth.models import User


# Create your models here.

 

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_massages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    class Meta:
        ordering = ['timestamp']

        def __str__(self):
            return f"de {self.sender.username} a {self.receiver.username}: {self.content[:50]}"
        
