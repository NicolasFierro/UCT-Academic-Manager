from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    image=models.ImageField(default="null")
    content = models.TextField()
    public = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now= True)

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    create_date = models.DateField()
    