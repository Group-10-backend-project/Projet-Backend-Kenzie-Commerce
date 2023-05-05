from django.db import models


class Cart(models.Model):
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name='cart'
    )
    product = models.ManyToManyField(
        "products.Product",
        related_name="cart"
    )
