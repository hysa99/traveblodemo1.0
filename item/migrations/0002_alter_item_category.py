# Generated by Django 4.1.7 on 2023-04-01 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="item.category",
            ),
        ),
    ]
