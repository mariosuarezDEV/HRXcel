from django.db import models

# Opciones de genero
GENERO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro')
)

# Opciones de estado civil
ESTADO_CIVIL = (
    ('S', 'Soltero'),
    ('C', 'Casado'),
    ('D', 'Divorciado'),
    ('V', 'Viudo')
)

# Opciones de escolaridad
ESCOLARIDAD = (
    ('P', 'Primaria'),
    ('S', 'Secundaria'),
    ('B', 'Bachillerato'),
    ('L', 'Licenciatura'),
    ('M', 'Maestria'),
    ('D', 'Doctorado')
)

class Empleado(models.Model):
    # Nombre
    primer_nombre = models.CharField(max_length=50, verbose_name="Primer nombre", null=False, blank=False)
    segundo_nombre = models.CharField(max_length=50, verbose_name="Segundo nombre", null=True, blank=True)
    primer_apellido = models.CharField(max_length=50, verbose_name="Primer apellido", null=False, blank=False)
    segundo_apellido = models.CharField(max_length=50, verbose_name="Segundo apellido", null=False, blank=False)
    
    # Contacto
    telefono = models.CharField(max_length=10, verbose_name="Telefono", null=True, blank=True)
    correo = models.EmailField(max_length=100, verbose_name="Correo", null=True, blank=True)
    
    # Ubicacion
    calle = models.CharField(max_length=100, verbose_name="Calle", null=True, blank=True)
    numero_exterior = models.CharField(max_length=10, verbose_name="Numero exterior", null=True, blank=True)
    numero_interior = models.CharField(max_length=10, verbose_name="Numero interior", null=True, blank=True)
    colonia = models.CharField(max_length=100, verbose_name="Colonia", null=True, blank=True)
    codigo_postal = models.CharField(max_length=5, verbose_name="Codigo postal", null=True, blank=True)
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad", null=True, blank=True)
    estado = models.CharField(max_length=100, verbose_name="Estado", null=True, blank=True)
    pais = models.CharField(max_length=100, verbose_name="Pais", null=True, blank=True)
    
    # Informacion personal
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", null=True, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO, verbose_name="Genero", null=True, blank=True)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL, verbose_name="Estado civil", null=True, blank=True)
    escolaridad = models.CharField(max_length=1, choices=ESCOLARIDAD, verbose_name="Escolaridad", null=True, blank=True)
    
    # Auditoria
    fecha_creacion = models.DateField(verbose_name="Fecha de creacion", null=True, blank=True, auto_now_add=True)
    fecha_modificacion = models.DateField(verbose_name="Fecha de modificacion", null=True, blank=True, auto_now=True)