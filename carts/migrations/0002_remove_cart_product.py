# Generated by Django 4.2.1 on 2023-05-08 12:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="product",
        ),
    ]