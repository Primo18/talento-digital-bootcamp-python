from django.db import models


# Create your models here.
class Conductor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"{self.rut} - {self.nombre} {self.apellido}"


class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    departamento = models.CharField(max_length=10, null=True, blank=True)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    conductor = models.OneToOneField(
        Conductor, on_delete=models.CASCADE, primary_key=True
    )

    def __str__(self):
        return (
            f"{self.calle} {self.numero}, {self.comuna}, {self.ciudad}, {self.region}"
        )


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    ano = models.IntegerField(null=False, blank=False)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo} {self.ano}"
