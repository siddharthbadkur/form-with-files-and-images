from django.db import models


# Create your models here.
class resume(models.Model):
    Name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    contact=models.IntegerField()
    image=models.ImageField(upload_to='image/')
    resume=models.FileField(upload_to='file/')

    
