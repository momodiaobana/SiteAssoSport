# Generated by Django 4.1.5 on 2023-02-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAsso', '0007_rename_stock_products_delete_basketp_delete_boxep_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
