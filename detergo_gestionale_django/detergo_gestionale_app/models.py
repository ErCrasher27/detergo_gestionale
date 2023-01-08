from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16, null=True)
    address = models.CharField(max_length=128, null=True)
    notes = models.CharField(max_length=256, null=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name + " " + self.last_name


class Order(models.Model):
    state = [
        ('NS', 'not_started'),
        ('PA', 'partial'),
        ('CO', 'completed')
    ]
    current_date = models.DateTimeField(auto_now=True)
    pickup_date = models.DateField()
    total = models.FloatField()
    credit = models.FloatField()
    domicile = models.BooleanField()
    state = models.CharField(max_length=2, choices=state)
    notes = models.CharField(max_length=256)
    id_customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='get_customer')

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.current_date


class Category(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_icon(self):
        if self.icon:
            return 'http://127.0.0.1:8000' + self.icon.url
        return ''

class Item(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='uploads/', blank=True, max_length=256)
    water_price = models.FloatField()
    dry_price = models.FloatField()
    tailoring_price = models.FloatField()
    id_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='get_category')

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='uploads/', blank=True, max_length=256)

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return self.name


class Defect(models.Model):
    nome = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='uploads/', blank=True, max_length=256)

    class Meta:
        verbose_name = "Defect"
        verbose_name_plural = "Defects"

    def __str__(self):
        return self.nome


class BroughtItem(models.Model):
    state = [
        ('NS', 'not_started'),
        ('PA', 'partial'),
        ('CO', 'completed')
    ]
    state = models.CharField(max_length=2, choices=state)
    price = models.FloatField(null=True)
    photo = models.ImageField(upload_to='uploads/',
                              blank=True, max_length=256, null=True)
    id_order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='get_order')
    id_item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='get_item')
    color = models.ManyToManyField(Color)
    defect = models.ManyToManyField(Defect)

    class Meta:
        verbose_name = "BroughtItem"
        verbose_name_plural = "CarriedItems"

    def __str__(self):
        return self.id_order + " " + self.id_item
