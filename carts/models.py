from django.db import models


class Cart(models.Model):
    is_active = models.BooleanField(default=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name='cart'
    )

    products = models.ManyToManyField(
        "products.Product",
        through='carts.CartProduct',
        related_name='cart_products'
    )


class CartProduct(models.Model):

    cart = models.ForeignKey("carts.Cart", on_delete=models.CASCADE)

    products = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    amount = models.PositiveIntegerField()
