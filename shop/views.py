from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Products
from .addform import AddForm

# Create your views here.
def index(request):
    products = Products.objects.all()
    return render(request, 'shop/index.html', {'products':products})

def product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'shop/product.html', {'product':product})

def add_product(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auther = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('product', pk=post.pk)
    else:
        form = AddForm()
    return render(request, 'shop/add_product.html', {'form': form})

def edit_product(request, pk):
    post = get_object_or_404(Products, pk=pk)
    if request.method == "POST":
        form = AddForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.auther = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('product', pk=post.pk)
    else:
        form = AddForm(instance=post)
    return render(request, 'shop/add_product.html', {'form': form})


