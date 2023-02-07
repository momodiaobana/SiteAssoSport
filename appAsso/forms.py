from django import forms
from django.forms import ModelForm
from .models import Products


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ('nomProduit', 'prix','cProduit')
        labels = {
            'nomProduit':'', 
            'prix':'', 
            'cProduit':'', 
        }
        widgets = {
            'nomProduit': forms.TextInput(attrs={}),
            'prix' : forms.TextInput(attrs={}),
            'cProduit' : forms.TextInput(attrs={}),
        }
