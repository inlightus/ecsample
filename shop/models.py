from django.db import models
from django.utils import timezone

# Create your models here.

class Products(models.Model):
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=15)
    description = models.TextField()
    stock = models.PositiveSmallIntegerField()
    seller_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.product
