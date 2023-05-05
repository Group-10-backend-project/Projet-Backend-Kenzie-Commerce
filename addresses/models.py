from django.db import models


class Address(models.Model):

    street = models.CharField(max_length=127)
    number = models.IntegerField(max_length=10)
    city = models.CharField(max_length=55)

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE
    )
