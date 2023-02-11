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
    
    
    #generation d'une cle unique pour l'image
    def key_generator() -> str:
        liste = []
        for i in range(6):
            if i % 2 == 0:
                liste.append(random.choice(string.ascii_lowercase))
            else:
                liste.append(random.randint(0, 9))
                liste.append(random.choice(string.ascii_uppercase))

        for i in range(len(liste)):
            if type(liste[i]) is int:
                liste[i] = str(liste[i])

        return "".join(liste)

#faire une nouvelle base ajoutant une description et supprimer la quantité 
'''class basketP(models.Model):        
    nomProduit = models.CharField(max_length= 45, null = False)
    prix = models.FloatField(default=0.0, null = False)

class footP(models.Model):        
    nomProduit = models.CharField(max_length= 45, null = False)
    prix = models.FloatField(default=0.0, null = False)

class boxeP(models.Model):        
    nomProduit = models.CharField(max_length= 45, null = False)
    prix = models.FloatField(default=0.0, null = False)
'''
