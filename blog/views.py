from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from blog.models import Ingresar_variables
import os
import pickle

# Create your views here.
def ingresar_variables(request):
    return render(request, 'blog/ingresar_variables.html', {})

def resultado(request):
    if request.method == 'GET':
        #form = PostForm(request.GET)
        # if form.is_valid():
        #     post = form.save(commit=False)
        #     post.save()
        # return HttpResponseRedirect('/resultado')
        #    return redirect('resultado', pk=resultado.pk)
        bolsas = request.GET['bolsas']
        sexo = request.GET['sexo']
        edad = request.GET['edad']
        peso = request.GET['peso']
        diagnostico = request.GET['diagnostico']
        servicio = request.GET['servicio']
        hemoglobina = request.GET['hemoglobina']
        hematocrito = request.GET['hematocrito']
        gsreceptor = request.GET['gsreceptor']
        gsdonante = request.GET['gsdonante']
        hiv = request.GET['hiv']
        hb = request.GET['hb']
        antihb = request.GET['antihb']
        antihcv = request.GET['antihcv']
        htlv = request.GET['htlv']
        sifilis = request.GET['sifilis']
        chagas = request.GET['chagas']
        inputs = [int(bolsas), int(sexo), int(edad), int(peso), int(diagnostico), int(servicio), int(hemoglobina), int(hematocrito), int(gsreceptor), int(gsdonante), int(hiv), int(hb), int(antihb), int(antihcv), int(htlv), int(sifilis), int(chagas)]
        print(inputs)
        salida = calculo(inputs)
        print(salida)

        return render(request, 'blog/resultado.html',{'bolsas':bolsas, 'sexo':sexo, 'edad':edad, 'peso':peso, 'diagnostico':diagnostico, 'servicio':servicio, 'hemoglobina':hemoglobina, 'hematocrito':hematocrito, 'gsreceptor':gsreceptor, 'gsdonante':gsdonante, 'hiv':hiv, 'hb':hb, 'antihb':antihb, 'antihcv':antihcv, 'htlv':htlv, 'sifilis':sifilis, 'chagas':chagas, 'salida':salida})
        
    else:
        #form = PostForm()
        return HttpResponse('ERROR')
    #return render(request, 'blog/resultado.html', {'form': form})

def calculo(inputs):
    #numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    list_pickle_path = 'modelo.sav'
    
    # Create an variable to pickle and open it in write mode
    list_pickle = open(list_pickle_path, 'wb')
    salida = pickle.dump(inputs, list_pickle)
    list_pickle.close()
    return salida