# Generated by Django 4.1.1 on 2022-09-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0006_alter_employee_date_creation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="type",
            name="name",
            field=models.CharField(max_length=50, unique=True, verbose_name="Nombre"),
        ),
    ]
