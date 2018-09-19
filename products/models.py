from django.db import models

# Create your models here.
class ProductType(models.Model):
    TYPES = (
        ('Laptops', 'Laptops'),
        ('Tablets', 'Tablets'),
        ('Printers', 'Printers'),
        ('Accessories', 'Accessories')

    )
    name = models.CharField(max_length=12, choices=TYPES)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    price = models.FloatField(max_length=10)
    inventory = models.IntegerField()
    description = models.TextField(max_length=200)
    imageURL = models.CharField(max_length=50)

    def __str__(self):
        return self.name
