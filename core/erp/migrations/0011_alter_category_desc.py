# Generated by Django 4.1.1 on 2022-10-11 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0010_alter_category_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="desc",
            field=models.TextField(
                blank=True, max_length=200, null=True, verbose_name="Descripción"
            ),
        ),
    ]