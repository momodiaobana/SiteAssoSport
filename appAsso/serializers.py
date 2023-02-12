from rest_framework.serializers import ModelSerializer
from appAsso.models import Products

class ProductSerializer(ModelSerializer): 
    class Meta: 
        model = Products
        fields = ['id', 'nomProduit', 'prix', 'cProduit', 'description']
