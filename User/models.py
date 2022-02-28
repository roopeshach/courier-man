from django.db import models

# Create your models here.

class OTP(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.otp)