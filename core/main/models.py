from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField("Caregory name", max_length=30, default=None)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField("Product name", max_length=50)
    price = models.BigIntegerField("Product price")
    image = models.ImageField("Product image", upload_to="images")

    def __str__(self):
        return f"{self.name}"
