from django import forms
from empleado.models import Empleado
from empleado.models import Usuario
from empleado.models import Rol


class EmpleadoForm(forms.ModelForm):
    class Meta: #   Modelo que debe ser utilizado para crear el formulario
        model= Empleado
        fields= '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields= '__all__'

class RolForm(forms.ModelForm):
    class Meta:
        model= Rol
        fields= '__all__'