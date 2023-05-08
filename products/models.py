from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=127)
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='products',
    )
