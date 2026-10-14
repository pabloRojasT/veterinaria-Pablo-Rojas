from django.contrib import admin
from .models import Atencion, Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ("nombre", "apellido", "telefono", "correo")
	list_filter = ("apellido",)
	search_fields = ("nombre", "apellido", "telefono", "correo")


@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
	list_display = ("titulo", "cliente", "fecha", "monto_en_pesos")
	list_filter = ("fecha", "cliente")
	search_fields = (
		"titulo",
		"descripcion",
		"cliente__nombre",
		"cliente__apellido",
	)

	@admin.display(description="Monto (CLP)", ordering="monto")
	def monto_en_pesos(self, obj):
		monto = f"{obj.monto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
		if monto.endswith(",00"):
			monto = monto[:-3]
		return f"${monto}"
