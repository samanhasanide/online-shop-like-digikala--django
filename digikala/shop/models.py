from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Category(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField(
        upload_to='upload/category/', blank=True, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(
        max_length=500, default='', blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    existance = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='upload/product/')

    COLORS = (
        ('r', 'red'),
        ('w', 'white'),
        ('rg', 'rosegold'),
    )
    color = models.CharField(max_length=4, choices=COLORS, default='white')
    star = models.IntegerField(default=0, validators=[
                               MinValueValidator(0), MaxValueValidator(5)])
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(
        default=0, decimal_places=2, max_digits=12)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(
        max_length=500, default='', blank=False)
    phone = models.CharField(max_length=20, blank=True)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
