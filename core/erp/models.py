from django.db import models
from datetime import datetime

# Create your models here.


class Employee(models.Model):
    """Model definition for Employee."""
    # TODO: Define fields here
    names = models.CharField(max_length=150, verbose_name="Nombres")
    dni = models.CharField(max_length=10, verbose_name="DNI", unique=True)
    date_joined = models.DateField(
        default=datetime.now, verbose_name="Fecha de registro")
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(
        upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    cvitae = models.FileField(
        upload_to="cvitae/%Y/%m/%d", null=True, blank=True)

    class Meta:
        """Meta definition for Employee."""
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']

    def __str__(self):
        """Unicode representation of Employee."""
        return self.names
