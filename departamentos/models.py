from django.db import models

# Departamento o area de la empresa

class Departamento(models.Model):
    # Información
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripcion", null=True, blank=True)
    
    # Ubicación
    calle = models.CharField(max_length=100, verbose_name="Calle", null=True, blank=True)
    numero_exterior = models.CharField(max_length=10, verbose_name="Numero exterior", null=True, blank=True)
    numero_interior = models.CharField(max_length=10, verbose_name="Numero interior", null=True, blank=True)
    colonia = models.CharField(max_length=100, verbose_name="Colonia", null=True, blank=True)
    codigo_postal = models.CharField(max_length=5, verbose_name="Codigo postal", null=True, blank=True)
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad", null=True, blank=True)
    estado = models.CharField(max_length=100, verbose_name="Estado", null=True, blank=True)
    pais = models.CharField(max_length=100, verbose_name="Pais", null=True, blank=True)
    
    # Contacto
    telefono = models.CharField(max_length=10, verbose_name="Telefono", null=True, blank=True)
    correo = models.EmailField(max_length=100, verbose_name="Correo", null=True, blank=True)
    
    # Detalle
    gerente = models.IntegerField(verbose_name="Gerente", null=True, blank=True) # ID del gerente del departamento
    
    # Presupuesto
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Presupuesto mensual", null=True, blank=True) # Cantidad de dinero que se tiene para gastar en el departamento
    
    # Auditoria
    fecha_creacion = models.DateField(verbose_name="Fecha de creacion", null=True, blank=True, auto_now_add=True)
    fecha_modificacion = models.DateField(verbose_name="Fecha de modificacion", null=True, blank=True, auto_now=True)
    
    