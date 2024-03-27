from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):  # при заказе продукта доставать по pk юзера и при создании ордера вставлять его
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer_id = models.BigIntegerField()
    address = models.TextField()

    def __str__(self):
        return self.product
