from django import forms

from .models import Products


class AddForm(forms.ModelForm):


    class Meta:
        model = Products
        fields = (
                'product',
                'price',
                'description',
                'stock',
                'seller_name',
                )

