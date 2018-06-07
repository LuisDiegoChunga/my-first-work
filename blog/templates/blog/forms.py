from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('numero_bolsas', 'sexo', 'edad', 'peso', 'diagnostico', 'servicio', 'hemoglobina', 'hematocrito', 'gs_receptor', 'gs_donante', 'hiv', 'hb', 'anti_hb', 'anti_hcv', 'htlv', 'sifilis', 'chagas')
        