from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Products
from .forms import AddForm

# Create your views here.
def index(request):
    products = Products.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'shop/index.html', {'products':products})

def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'shop/product_detail.html', {'product':product})

@login_required
def product_new(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('product_detail', pk=post.pk)
    else:
        form = AddForm()
    return render(request, 'shop/product_edit.html', {'form': form})

@login_required
def product_edit(request, pk):
    post = get_object_or_404(Products, pk=pk)
    if request.method == "POST":
        form = AddForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('product_detail', pk=post.pk)
    else:
        form = AddForm(instance=post)
    return render(request, 'shop/product_edit.html', {'form': form})

@login_required
def product_draft_list(request):
    products = Products.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'shop/product_draft_list.html', {'products': products})

@login_required
def product_publish(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.publish()
    return redirect('product_detail', pk=pk)

def publish(self):
    self.published_date = timezone.now()
    self.save()

@login_required
def product_remove(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return redirect('index')
