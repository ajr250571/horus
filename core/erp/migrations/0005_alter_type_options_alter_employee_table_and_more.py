# Generated by Django 4.1.1 on 2022-09-30 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0004_alter_type_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="type",
            options={
                "managed": True,
                "ordering": ["id"],
                "verbose_name": "Tipo",
                "verbose_name_plural": "Tipos",
            },
        ),
        migrations.AlterModelTable(
            name="employee",
            table=None,
        ),
        migrations.AlterModelTable(
            name="type",
            table=None,
        ),
    ]
