from django.db import models

# Create your models here.


class OrderOptions(models.TextChoices):
    PEDIDO_REALIZADO = "PEDIDO REALIZADO"

    EM_ANDAMENTO = "EM ANDAMENTO"

    ENTREGUE = "ENTREGUE"

    DEFAULT = "ADICIONE UM STATUS"


class Order(models.Model):
    status = models.CharField(
        max_length=127, choices=OrderOptions, default=OrderOptions.DEFAULT
    )

    created_at = models.DateField(auto_now_add=True)
