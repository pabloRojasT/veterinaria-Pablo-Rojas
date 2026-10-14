from django.db import models


class Cliente(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	telefono = models.CharField(max_length=20)
	correo = models.EmailField()
	direccion = models.CharField(max_length=255)

	def __str__(self):
		return f"{self.nombre} {self.apellido}"


class Atencion(models.Model):
	cliente = models.ForeignKey(
		Cliente,
		on_delete=models.CASCADE,
		related_name="atenciones",
	)
	titulo = models.CharField(max_length=150)
	descripcion = models.TextField()
	fecha = models.DateField(auto_now_add=True)
	monto = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return f"{self.titulo} - {self.cliente}"
