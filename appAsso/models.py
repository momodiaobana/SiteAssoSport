from django.db import models

# Create your models here.


class Stock(models.Model):
    nomProduit = models.CharField(max_length= 45, null = False)
    prix = models.FloatField(default=0.0, null = False)
    cProduit = models.CharField(max_length=45, null = False)
    

class basketP(models.Model):        
    nomProduit = models.CharField(max_length= 45, null = False)
    prix = models.FloatField(default=0.0, null = False)

class footP(models.Model):        
    nomProduit = models.CharField(max_length= 45, null = False)
    prix = models.FloatField(default=0.0, null = False)

class boxeP(models.Model):        
    nomProduit = models.CharField(max_length= 45, null = False)
    prix = models.FloatField(default=0.0, null = False)

