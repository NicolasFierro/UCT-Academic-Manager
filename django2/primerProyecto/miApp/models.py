from django.db import models

# Create your models here.
class Article(models.Model):
    userName = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    password = models.TextField()
    phone = models.BooleanField()
    upload_to="articles"

class Category(models.Model):
    userName = models.CharField(max_length=110)
    description = models.CharField(max_length=250)

class Meta:
    #db_table=""
    verbose_name="Articulo"
    verbose_name_plural="Articulos"
    #Ordenamos de forma ascendente los articulos
    ordering=['id']
    def _str_(self):
        if self.public:
            publico="(Publico)"
        else:
            publico="(Privado)"
        return f"{self.id}-{self.title} : {publico}"


