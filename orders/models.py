from django.db import models


class OrderOptions(models.TextChoices):
    PEDIDO_REALIZADO = "PEDIDO REALIZADO"

    EM_ANDAMENTO = "EM ANDAMENTO"

    ENTREGUE = "ENTREGUE"

    DEFAULT = "ADICIONE UM STATUS"


class Order(models.Model):
    status = models.CharField(
        max_length=127, choices=OrderOptions.choices, default=OrderOptions.DEFAULT
    )

    created_at = models.DateField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="Orders"
    )

    saller = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="Saller"
    )

    cart = models.ForeignKey(
        "carts.Cart", on_delete=models.PROTECT, related_name="Cart"
    )
