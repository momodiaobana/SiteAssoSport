from django.db import models
import random, string 
# Create your models here.


class Products(models.Model):
    nomProduit = models.CharField(max_length=45, null=False)
    prix = models.FloatField(default=0.0, null=False)
    cProduit = models.CharField(max_length=45, null=False)
    description = models.TextField(max_length=128, null=True)
    img = models.ImageField(upload_to="media", blank=True)


    def __str__(self) -> str:
        return self.nomProduit
    

