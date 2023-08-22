from django.db.models.signals import pre_save
from django.utils import timezone
from django.db import models
from bases.models import ClaseModelo


class Proyecto(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Nombre del proyecto', unique=True)
    contacto = models.CharField(max_length=100, help_text='Nombre del contacnto en territorio')
    telefono = models.CharField(max_length=16, help_text='Telefono')
    email = models.EmailField()
    donante = models.CharField(max_length=250, blank=True, null=True, help_text='Ente donante')
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField()
    
    directa = 'DIRECTA'
    socio ='SOCIO'
    forma_ejecucion = [
        (directa,'DIRECTA'),
        (socio,'SOCIO'),
    ]
    ejecucion = models.CharField(
        max_length=7,
        choices=forma_ejecucion,
        default=directa
    )
    nombre_socio = models.CharField(max_length=250, help_text='Nombre del socio', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        self.contacto = self.contacto.upper()
        if self.donante:
            self.donante = self.donante.upper()
            if self.nombre_socio:
                self.nombre_socio = self.nombre_socio.upper()
        super(Proyecto, self).save(*args, **kwargs)


class Meta:
    verbose_name_plural = "Proyectos"

# Función para actualizar el estado
def actualizar_estado_proyecto(sender, instance, **kwargs):
    ahora = timezone.now()
    if instance.fechaFin < ahora:
        instance.estado = False
    else:
        instance.estado = True
# Registra la señal
pre_save.connect(actualizar_estado_proyecto, sender=Proyecto)



class Pnd(ClaseModelo): 
    descripcion = models.CharField(max_length=100, help_text='Prioridad Nacional de Desarrollo', unique=True)
    def __str__(self):
        return'{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Pnd, self).save()
    
    class Meta:
        verbose_name_plural = "Prioridades "

class Departamento(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Nombre del departamento', unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()#Pone en mayusculas la cadena de tedxto ingresada
        super(Departamento, self).save()
    
    class Meta:
        verbose_name_plural = "Departamento"

class Municipio(ClaseModelo):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format( self.descripcion)
       

    def save(self):
        self.descripcion = self.descripcion.upper()#Pone en mayusculas la cadena de tedxto ingresada
        super(Municipio, self).save()
    
    class Meta:
        verbose_name_plural = "Municipios"
        unique_together = ('departamento','descripcion')
        ordering = ['descripcion']

class Comunidad(ClaseModelo):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format( self.descripcion)
       

    def save(self):
        self.descripcion = self.descripcion.upper()#Pone en mayusculas la cadena de tedxto ingresada
        super(Comunidad, self).save()
    
    class Meta:
        verbose_name_plural = "Comunidades"
        unique_together = ('municipio','descripcion')
        ordering = ['descripcion']

class Pueblo(ClaseModelo):
    descripcion = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Pueblo, self).save()
    
    class Meta:
        verbose_name_plural = "Pueblos"
        ordering = ['descripcion']

        
class Poblacion(ClaseModelo):
    descripcion = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Poblacion, self).save()
    
    class Meta:
        verbose_name_plural = "Poblaciones"
        ordering = ['descripcion']
        

class ProyectoDetalle(ClaseModelo):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100, help_text='Nombre del programa')
    objetivo = models.CharField(max_length=900, help_text='Objetivo')
    cantidad_beneficiados = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    comunidad = models.ManyToManyField(Comunidad)
    pueblo = models.ForeignKey(Pueblo, on_delete=models.CASCADE, null=True, blank=True)
    poblacion = models.ForeignKey(Poblacion, on_delete=models.CASCADE)
    
    montoPND1 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaPND1 = models.CharField(max_length=500, blank=True, null=True)
    indicadorPND1 = models.CharField(max_length=500, blank=True, null=True)
    montoPND2 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaPND2 = models.CharField(max_length=500, blank=True, null=True)
    indicadorPND2 = models.CharField(max_length=500, blank=True, null=True)
    montoPND3 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaPND3 = models.CharField(max_length=500, blank=True, null=True)
    indicadorPND3 = models.CharField(max_length=500, blank=True, null=True)
    montoPND4 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaPND4 = models.CharField(max_length=500, blank=True, null=True)
    indicadorPND4 = models.CharField(max_length=500, blank=True, null=True)
    montoPND5 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaPND5 = models.CharField(max_length=500, blank=True, null=True)
    indicadorPND5 = models.CharField(max_length=500, blank=True, null=True)
    montoPND6 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaPND6 = models.CharField(max_length=500, blank=True, null=True)
    indicadorPND6 = models.CharField(max_length=500, blank=True, null=True)
    montoPND7 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaPND7 = models.CharField(max_length=500, blank=True, null=True)
    indicadorPND7 = models.CharField(max_length=500, blank=True, null=True)
    montoPND8 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaPND8 = models.CharField(max_length=500, blank=True, null=True)
    indicadorPND8 = models.CharField(max_length=500, blank=True, null=True)
    montoPND9 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaPND9 = models.CharField(max_length=500, blank=True, null=True)
    indicadorPND9 = models.CharField(max_length=500, blank=True, null=True)
    montoPND10 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaPND10 = models.CharField(max_length=500, blank=True, null=True)
    indicadorPND10 = models.CharField(max_length=500, blank=True, null=True)

    PNDOtro1 = models.CharField(max_length=500, blank=True, null=True)
    montoOtro1 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaOtro1 = models.CharField(max_length=500, blank=True, null=True)
    indicadorOtro1 = models.CharField(max_length=500, blank=True, null=True)

    PNDOtro2 = models.CharField(max_length=500, blank=True, null=True)
    montoOtro2 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaOtro2 = models.CharField(max_length=500, blank=True, null=True)
    indicadorOtro2 = models.CharField(max_length=500, blank=True, null=True)

    PNDOtro3 = models.CharField(max_length=500, blank=True, null=True)
    montoOtro3 = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    metaOtro3 = models.CharField(max_length=500, blank=True, null=True)
    indicadorOtro3 = models.CharField(max_length=500, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        self.objetivo = self.objetivo.upper() if self.objetivo else None

        self.metaPND1 = self.metaPND1.upper() if self.metaPND1 else None
        self.indicadorPND1 = self.indicadorPND1.upper() if self.indicadorPND1 else None
        self.metaPND2 = self.metaPND2.upper() if self.metaPND2 else None
        self.indicadorPND2 = self.indicadorPND2.upper() if self.indicadorPND2 else None
        self.metaPND3 = self.metaPND3.upper() if self.metaPND3 else None
        self.indicadorPND3 = self.indicadorPND3.upper() if self.indicadorPND3 else None
        self.metaPND4 = self.metaPND4.upper() if self.metaPND4 else None
        self.indicadorPND4 = self.indicadorPND4.upper() if self.indicadorPND4 else None
        self.metaPND5 = self.metaPND5.upper() if self.metaPND5 else None
        self.indicadorPND5 = self.indicadorPND5.upper() if self.indicadorPND5 else None
        self.metaPND6 = self.metaPND6.upper() if self.metaPND6 else None
        self.indicadorPND6 = self.indicadorPND6.upper() if self.indicadorPND6 else None
        self.metaPND7 = self.metaPND7.upper() if self.metaPND7 else None
        self.indicadorPND7 = self.indicadorPND7.upper() if self.indicadorPND7 else None
        self.metaPND8 = self.metaPND8.upper() if self.metaPND8 else None
        self.indicadorPND8 = self.indicadorPND8.upper() if self.indicadorPND8 else None
        self.metaPND9 = self.metaPND9.upper() if self.metaPND9 else None
        self.indicadorPND9 = self.indicadorPND9.upper() if self.indicadorPND9 else None
        self.metaPND10 = self.metaPND10.upper() if self.metaPND10 else None
        self.indicadorPND10 = self.indicadorPND10.upper() if self.indicadorPND10 else None

        self.PNDOtro1 = self.PNDOtro1.upper() if self.PNDOtro1 else None
        self.metaOtro1 = self.metaOtro1.upper() if self.metaOtro1 else None
        self.indicadorOtro1 = self.indicadorOtro1.upper() if self.indicadorOtro1 else None

        self.PNDOtro2 = self.PNDOtro2.upper() if self.PNDOtro2 else None
        self.metaOtro2 = self.metaOtro2.upper() if self.metaOtro2 else None
        self.indicadorOtro2 = self.indicadorOtro2.upper() if self.indicadorOtro2 else None

        self.PNDOtro3 = self.PNDOtro3.upper() if self.PNDOtro3 else None
        self.metaOtro3 = self.metaOtro3.upper() if self.metaOtro3 else None
        self.indicadorOtro3 = self.indicadorOtro3.upper() if self.indicadorOtro3 else None

        super().save(*args, **kwargs)

            
    class Meta:
        verbose_name_plural = "Detalle Proyectos"
        #unique_together = ('municipio', 'poblacion')




