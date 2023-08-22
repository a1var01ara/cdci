from django import forms

from .models import Proyecto, ProyectoDetalle, Pnd, Departamento, Municipio, Comunidad,\
      Pueblo, Poblacion

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['descripcion','contacto', 'telefono','email','fechaInicio','fechaFin','donante','ejecucion','nombre_socio','estado']

        labels = {'descripcion': "Nombre del Proyecto",
                  'contacto': "Nombre del Contacto",
                  'email': "Correo del Contacto",
                  'telefono': "Telefono del Contacto",
                  'fechaInicio':"Fecha Inicio",
                  'fechaFin':"Fecha Fin",
                  'donante': "Donante",
                  'ejecucion': "Forma Ejecucion",
                  'nombre_socio': "Nombre del Socio",
                  "estado": "Estado"}
                  
        widget = {'descripcion': forms.TextInput}
       

    def clean(self):
        try:
            sc = Proyecto.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper(),
                
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro ya existe")
            elif self.instance.pk!=sc.pk:
                
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Proyecto.DoesNotExist:
            pass
        
        return self.cleaned_data  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['estado'].widget.attrs['disabled'] = True
        


class ProyectoDetalleForm(forms.ModelForm):  
    class Meta:
        model=ProyectoDetalle
        fields=['descripcion','objetivo','cantidad_beneficiados','departamento', 'municipio','comunidad','pueblo','poblacion', \
                 'montoPND1','metaPND1','montoPND2','metaPND2','montoPND3','metaPND3','montoPND4','metaPND4','montoPND5','metaPND5','montoPND6','metaPND6', \
                    'montoPND7','metaPND7','montoPND8','metaPND8', 'montoPND9','metaPND9','montoPND10','metaPND10', \
                        'indicadorPND1','indicadorPND2','indicadorPND3','indicadorPND4','indicadorPND5','indicadorPND6','indicadorPND7','indicadorPND8','indicadorPND9','indicadorPND10', \
                        'montoOtro1', 'montoOtro2', 'montoOtro3', 'metaOtro1', 'metaOtro2', 'metaOtro3', 'indicadorOtro1',  'indicadorOtro2',  'indicadorOtro3', \
                                 'PNDOtro1', 'PNDOtro2', 'PNDOtro3',    ]
        exclude=['estado']
        widgets = {
            'comunidad': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.helper = helper.FormHelper()
        #self.helper.form_id = "myform"
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
    
   





class PndForm(forms.ModelForm):
    class Meta:
        model = Pnd
        fields = ['descripcion','estado']

        labels = {'descripcion': "Nombre de la Prioridad",
                  "estado": "Estado"}
                  
        widget = {'descripcion': forms.TextInput}

    def clean(self):
        try:
            sc = Pnd.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )
 
            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro ya existe")
            elif self.instance.pk!=sc.pk:
                
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Pnd.DoesNotExist:
            pass
        return self.cleaned_data  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['descripcion','estado']

        labels = {'descripcion': "Nombre de la comunidad",
                  "estado": "Estado"}
                  
        widget = {'descripcion': forms.TextInput}

    def clean(self):
        try:
            sc = Departamento.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro ya existe")
            elif self.instance.pk!=sc.pk:
                
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Departamento.DoesNotExist:
            pass
        return self.cleaned_data  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class MunicipioForm(forms.ModelForm):
    departamento = forms.ModelChoiceField(
        queryset=Departamento.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model = Municipio
        fields = ['departamento','descripcion', 'estado']

        labels = {'descripcion': "Nombre de la comunidad",
                  "estado": "Estado"}
                  
        widget = {'descripcion': forms.TextInput}

    def clean(self):
        try:
            sc = Municipio.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper(),
                departamento =self.cleaned_data["departamento"]
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro ya existe")
            elif self.instance.pk!=sc.pk:
                
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Municipio.DoesNotExist:
            pass
        return self.cleaned_data  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['departamento'].empty_label = "Seleccione Departamento"

class PuebloForm(forms.ModelForm):
    class Meta:
        model = Pueblo
        fields = ['descripcion','estado']

        labels = {'descripcion': "Nombre del pueblo",
                  "estado": "Estado"}
                  
        widget = {'descripcion': forms.TextInput}

    def clean(self):
        try:
            sc = Pueblo.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro ya existe")
            elif self.instance.pk!=sc.pk:
                
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Pueblo.DoesNotExist:
            pass
        return self.cleaned_data  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class PoblacionForm(forms.ModelForm):
    class Meta:
        model = Poblacion
        fields = ['descripcion','estado']

        labels = {'descripcion': "Nombre de la población",
                  "estado": "Estado"}
                  
        widget = {'descripcion': forms.TextInput}

    def clean(self):
        try:
            sc = Poblacion.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro ya existe")
            elif self.instance.pk!=sc.pk:
                
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Poblacion.DoesNotExist:
            pass
        return self.cleaned_data  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ComunidadForm(forms.ModelForm):
    class Meta:
        model = Comunidad
        fields = ['municipio','descripcion', 'estado']

        labels = {'descripcion': "Nombre de la comunidad",
                  'distancia': "Distancia en kilometros",
                  "estado": "Estado"}
                  
        widget = {'descripcion': forms.TextInput}

    def clean(self):
        cleaned_data = super().clean()
        descripcion = cleaned_data.get("descripcion")
        municipio = cleaned_data.get("municipio")

        if descripcion and municipio:
            try:
                existing_community = Comunidad.objects.get(
                    descripcion__iexact=descripcion.upper(), municipio=municipio
                )
                if not self.instance.pk or self.instance.pk != existing_community.pk:
                    raise forms.ValidationError("Una comunidad con este nombre ya existe para este municipio.")
            except Comunidad.DoesNotExist:
                pass

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    

