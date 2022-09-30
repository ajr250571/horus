# Generated by Django 4.1.1 on 2022-09-30 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0002_alter_employee_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "Tipo",
                "verbose_name_plural": "Tipos",
                "db_table": "tipo",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="employee",
            name="type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="erp.type",
                verbose_name="Tipo",
            ),
            preserve_default=False,
        ),
    ]
