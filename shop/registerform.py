from django import forms

from .models import Products


class RegisterForm(forms.ModelForm):


    class Meta:
        model = Products
        fileds = (
                'product_name',
                'price',
                'description',
                'stock',
                'seller_name',
                )

