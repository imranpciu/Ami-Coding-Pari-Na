from django.db import models

# Create your models here.
# User_Authentication/models.py
from django.contrib.auth.models import User

class KhojInputValue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_values = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user.username}, Timestamp: {self.timestamp}"
