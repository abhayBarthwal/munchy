from django.db import models
from pytz import timezone

class Category(models.Model):
    timestamp = models.DateTimeField()
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    available = models.IntegerField()

    def __str__(self):
        return self.name

class Bestseller(models.Model):
    timestamp = models.DateTimeField()
    description = models.CharField(max_length=200)
    item_id = models.IntegerField()
    available = models.IntegerField()

    def __str__(self):
        return self.item_id

class Display(models.Model):
    timestamp = models.DateTimeField()
    description = models.CharField(max_length=200, default="Show off")
    scroll1 = models.CharField(max_length=200)
    scroll2 = models.CharField(max_length=200)
    scroll3 = models.CharField(max_length=200)
    bestseller_id = models.IntegerField()
    weekly_id = models.IntegerField()
    available = models.IntegerField()

    def __str__(self):
        return self.description

class Item(models.Model):
    timestamp = models.DateTimeField()
    name = models.CharField(max_length=100)
    category_id = models.IntegerField()
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.FloatField(max_length=10)
    thumbnail = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    bestseller = models.IntegerField()
    weekly = models.IntegerField()
    available = models.IntegerField()

    def __str__(self):
        return self.name

class Orders(models.Model):
    timestamp = models.DateTimeField()
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    name = models.CharField(max_length=70)
    available = models.IntegerField()

    def __str__(self):
        return self.name

class Weekly(models.Model):
    timestamp = models.DateTimeField()
    description = models.CharField(max_length=200, default="Weekly famous")
    item_id = models.IntegerField()
    available = models.IntegerField()

    def __str__(self):
        return self.description
