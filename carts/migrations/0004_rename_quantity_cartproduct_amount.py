# Generated by Django 4.2.1 on 2023-05-08 19:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0003_cartproduct"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartproduct",
            old_name="quantity",
            new_name="amount",
        ),
    ]
