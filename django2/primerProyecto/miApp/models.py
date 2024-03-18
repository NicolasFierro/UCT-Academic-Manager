from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    image=models.ImageField(default="null")
    content = models.TextField()
    public = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add =True)
    update_date = models.DateField(auto_now =True)
    upload_to="articles"

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    create_date = models.DateField()

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


