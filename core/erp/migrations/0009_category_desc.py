# Generated by Django 4.1.1 on 2022-10-11 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0008_category_client_detsale_product_sale_delete_employee_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="desc",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Descripcion"
            ),
        ),
    ]
