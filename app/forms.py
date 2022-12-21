from django import forms

class PostreForm(forms.Form):

    nombre=forms.CharField(label="Nombre", max_length=50)
    vegano=forms.IntegerField(label="Vegano")
    cantidas_personas=forms.IntegerField(label="cantidad_personas")

class PrincipalForm(forms.Form):

    nombre=forms.CharField(label="Nombre", max_length=50)
    vegano=forms.IntegerField(label="Vegano")
    cantidas_personas=forms.IntegerField(label="cantidad_personas")