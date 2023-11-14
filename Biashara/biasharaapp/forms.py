from django import forms
from biasharaapp.models import Product


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'origin', 'color']
