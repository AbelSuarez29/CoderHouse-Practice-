from django import forms


class cliente(forms.Form):
    cliente = forms.CharField()
    apellido = forms.CharField()
    fecha_nacimiento = forms.IntegerField()
    pais_origen = forms.CharField()


class Pais(forms.Form):
    nombre = forms.CharField()
