from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=100)
    image=models.ImageField(upload_to='gallery')
    link=models.URLField(max_length=300,null=True)



class Skills(models.Model):
    name=models.CharField(max_length=50)
    