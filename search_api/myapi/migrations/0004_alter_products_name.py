# Generated by Django 4.2.16 on 2024-10-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapi", "0003_products_rating_products_rating_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="name",
            field=models.CharField(db_index=True, max_length=500),
        ),
    ]