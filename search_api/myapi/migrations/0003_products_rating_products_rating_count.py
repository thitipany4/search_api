# Generated by Django 4.2.16 on 2024-10-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapi", "0002_rename_categorys_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="products",
            name="rating_count",
            field=models.IntegerField(default=0),
        ),
    ]
