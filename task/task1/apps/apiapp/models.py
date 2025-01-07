from django.db import models

# Create your models here.
class pepoles(models.Model):
    p_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    