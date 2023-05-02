from django import forms
from .models import Clients, Products, Sellers
 
class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'email']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'sku']

class SellerForm(forms.ModelForm):
    class Meta:
        model = Sellers
        fields = ['name', 'email']
    busqueda = forms.CharField(label='Buscar producto', max_length=100)