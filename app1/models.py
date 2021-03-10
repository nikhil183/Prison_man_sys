from django.db import models

# Create your models here.
class Prisoner(models.Model):
    pic = models.ImageField(upload_to = "static/prisoners" ,null=True , blank=True)
    name = models.CharField(max_length=30 , null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=6 , null=True)
    state = models.CharField(max_length=20 , null=True)
    address = models.CharField(max_length=50 , null=True)
    case = models.CharField(max_length=20 , null=True)
    parole = models.CharField(max_length=30 , null=True)

    def __str__(self):
        return self.name
