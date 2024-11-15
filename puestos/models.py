from django.db import models

ESCOLARIDAD_CHOICES = (
    ('P', 'Primaria'),
    ('S', 'Secundaria'),
    ('B', 'Bachillerato'),
    ('L', 'Licenciatura'),
    ('M', 'Maestria'),
    ('D', 'Doctorado')
)

class Habilidad(models.Model):
    # Atributos
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripcion", null=True, blank=True)
   
    # Habilitado
    habilitado = models.BooleanField(verbose_name="Habilitado", null=False, blank=False, default=True)
   
    # Auditoria
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
   
    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
   
    def __str__(self):  # Corregido los asteriscos
        return self.nombre

class Puesto(models.Model):
    # Atributos
    titulo = models.CharField(max_length=100, verbose_name="Titulo", null=False, blank=False)
    descripcion = models.TextField(verbose_name="Descripcion", null=True, blank=True)
    salario_minimo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salario minimo", null=False, blank=False)
    salario_maximo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salario maximo", null=True, blank=True)
   
    # Detalles
    escolaridad_minima = models.CharField(max_length=1, choices=ESCOLARIDAD_CHOICES, verbose_name="Escolaridad minima", null=True, blank=True)
    experiencia_minima = models.IntegerField(verbose_name="Experiencia minima", null=True, blank=True)
   
    # Habilidades
    habilidades = models.ManyToManyField(Habilidad, verbose_name="Habilidades", blank=True)  # Removido null=True ya que es redundante en ManyToManyField
   
    # Habilitado
    habilitado = models.BooleanField(verbose_name="Habilitado", null=False, blank=False, default=True)
   
    # Auditoria
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
   
    class Meta:
        verbose_name = "Puesto"
        verbose_name_plural = "Puestos"
   
    def __str__(self):  # Corregido los asteriscos
        return self.titulo