from django.db import models


class Cart(models.Model):
    is_active = models.BooleanField(default=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name='cart'
    )


class CartProduct(models.Model):

    cart = models.ForeignKey("carts.Cart", on_delete=models.CASCADE)

    products = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()
