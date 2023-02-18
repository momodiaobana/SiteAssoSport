from django.test import TestCase
from appAsso.models import Products
from rest_framework.test import APITestCase
from django.urls import reverse_lazy

# Create your tests here.

class TestProducts(APITestCase):
    url = reverse_lazy('products-list')

    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    def test_list(self): 
        #creation d'un produit pour tester
        products = Products.objects.create(nomProduit='casque', cProduit="boxe")
        
        #on realise un appel GET
        response = self.client.get(self.url)
        #on verifie que le statuts code de response est 200 
        #en gros on vérifie qu'on peut GET 
        self.assertEqual(response.status_code, 200)

        #donnees ajoutées attendues 
        excepted = [
            {
                'id':products.id,
                'nomProduit':products.nomProduit, 
                'prix':products.prix, 
                'cProduit':products.cProduit,
                'description':products.description,
            }

        ]
        #on varifie que les données attendues sont sont bien les memes 
        #que celles contenues dans response == donnée attendues 
        self.assertEqual(excepted, response.json())
    
    def test_create(self):
        #On verifie qu'aucun produit n'existe 
        self.assertFalse(Products.objects.exists())
        response = self.client.post(self.url, data={'nomProduit':'test'})
        self.assertEqual(response.status_code, 405)
        #malgré le statut code 405 on vérifie quand meme  si rien n'a été crée 
        self.assertFalse(Products.objects.exists())
