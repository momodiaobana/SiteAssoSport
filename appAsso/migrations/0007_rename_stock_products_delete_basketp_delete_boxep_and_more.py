# Generated by Django 4.1.6 on 2023-02-01 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appAsso", "0006_stock_img_stock_quantite"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Stock",
            new_name="Products",
        ),
        migrations.DeleteModel(
            name="basketP",
        ),
        migrations.DeleteModel(
            name="boxeP",
        ),
        migrations.DeleteModel(
            name="footP",
        ),
    ]
