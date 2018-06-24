from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    bolsas = forms.CharField(label='Numero de bolsas', max_length=100)
    sexo = forms.CharField(label='Sexo', max_length=100)
    edad = forms.CharField(label='Edad', max_length=100)
    peso = forms.CharField(label='Peso', max_length=100)
    diagnostico = forms.CharField(label='Diagnostico', max_length=100)
    servicio = forms.CharField(label='Servicio', max_length=100)
    hemoglobina = forms.CharField(label='Hemoglobina', max_length=100)
    hematocrito = forms.CharField(label='Hematocrito', max_length=100)
    gsreceptor = forms.CharField(label='GS Receptor', max_length=100)
    gsdonante = forms.CharField(label='GS Donante', max_length=100)
    hiv = forms.CharField(label='HIV', max_length=100)
    hb = forms.CharField(label='HB', max_length=100)
    antihb = forms.CharField(label='Anti-HB', max_length=100)
    antihcv = forms.CharField(label='Anti-HCV', max_length=100)
    htlv = forms.CharField(label='HTLV', max_length=100)
    sifilis = forms.CharField(label='Sifilis', max_length=100)
    chagas = forms.CharField(label='Chagas', max_length=100)

    # class Meta:
    #     model = Post
    #     fields = ('numero_bolsas', 'sexo', 'edad', 'peso', 'diagnostico', 'servicio', 'hemoglobina', 'hematocrito', 'gs_receptor', 'gs_donante', 'hiv', 'hb', 'anti_hb', 'anti_hcv', 'htlv', 'sifilis', 'chagas')
    