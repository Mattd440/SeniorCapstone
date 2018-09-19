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
    name = models.CharField(max_length=50, db_index=True)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.PositiveIntegerField()
    description = models.TextField(max_length=200)
    available = models.BooleanField(default=True)
    imageURL = models.CharField(max_length=50)

    def __str__(self):
        return self.name
