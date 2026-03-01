from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    password = models.CharField(max_length=128)  

    def __str__(self):
        return self.user_name