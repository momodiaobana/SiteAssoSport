# Generated by Django 4.1.3 on 2023-02-01 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("nomProduit", models.CharField(max_length=45)),
                ("prix", models.FloatField(default=0.0)),
                ("cProduit", models.CharField(max_length=45)),
            ],
        ),
    ]
