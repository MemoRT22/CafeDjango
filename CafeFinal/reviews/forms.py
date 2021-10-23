from django.forms import widgets
from .models import Pedido
from django import forms

class PedidoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        total = self.request.session.get('total')
        # Ejecutar el constructor
        super().__init__(*args, **kwargs)

        # Inicializar el campo total
        self.fields["total"].initial = total

    class Meta:
        model = Pedido
        fields = ['correo', 'nombre', 'direccion', 'colonia', 'total']
        widgets = {
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección, calle y número'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia o fraccionamiento'}),
            'total': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }