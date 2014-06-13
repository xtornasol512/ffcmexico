# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301
from mail import mailing
import time

#Dicccionario ejemplo
my_data_dict= {'hola':"fatima"}
my_data = {'noenviado': "hola"}
#horario_actual = time.now()
"""
=====DIRECTORIO PRINCIPAL===========
"""

def index_view(request):
    #hora = time.strftime("%H")
    cxt = mailing(request, {})

    return render_to_response('home/index.html',
                          cxt,
                          context_instance=RequestContext(request))
#Privacidad
def terminos(request):
    return render_to_response('privacidad/terminos_privacidad.html',
                          my_data,
                          context_instance=RequestContext(request))

#Paginas Base
def contacto(request):
    return render_to_response('home/contacto.html',
                          my_data,
                          context_instance=RequestContext(request))

def sink(request):
    return render_to_response('blocks/sink.html',
                          my_data,
                          context_instance=RequestContext(request))
def horario(request):
    return render_to_response('home/horario.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def nosotros(request):
    return render_to_response('home/nosotros.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def codigoconducta(request):
    return render_to_response('home/codigo.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def faqs(request):
    return render_to_response('home/faqs.html',
                          my_data_dict,
                          context_instance=RequestContext(request))
def freeweek(request):
    return render_to_response('home/freeweek.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def maps(request):
    return render_to_response('home/mapa.html',
                          my_data_dict,
                          context_instance=RequestContext(request))
def galeria(request):
    return render_to_response('galeria/galeria.html',
                          my_data_dict,
                          context_instance=RequestContext(request))
#Galeria
def videos(request):
    return render_to_response('galeria/videos.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def fotos(request):
    return render_to_response('galeria/fotos.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

#Instructores
def brian(request):
    return render_to_response('instructores/brian.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def instructores(request):
    return render_to_response('instructores/instructores.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def pako(request):
    return render_to_response('instructores/pako.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def edu(request):
    return render_to_response('instructores/edu.html',
                          my_data_dict,
                          context_instance=RequestContext(request))
#Programas
def programas(request):
    return render_to_response('programas/programas.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def kids(request):
    return render_to_response('programas/kids.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def bjj(request):
    return render_to_response('programas/bjj.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def mma(request):
    return render_to_response('programas/mma.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def kids(request):
    return render_to_response('programas/kids.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def box(request):
    return render_to_response('programas/box.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def cross(request):
    return render_to_response('programas/cross.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def sumision(request):
    return render_to_response('programas/sumision.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def judo(request):
    return render_to_response('programas/judo.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

#Servicios
def servicios(request):
    return render_to_response('servicios/servicios.html',
                          my_data_dict,
                          context_instance=RequestContext(request))
def terapia(request):
    return render_to_response('servicios/terapia.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def nutricion(request):
    return render_to_response('servicios/nutricion.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

def masaje(request):
    return render_to_response('servicios/masaje.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

"""
=====REDIRECT's RULES===========
"""
#Redirect HOME
def galeriaRedirect(request):
  return redirect301('/galeria')
#Redirects Servicios
def videosRedirect(request):
    return redirect301('/galeria/videos')

def fotosRedirect(request):
    return redirect301('/galeria/fotos')

#Redirects Servicios
def terapiaRedirect(request):
    return redirect301('/servicios/fisioterapia')

def masajeRedirect(request):
    return redirect301('/servicios/masaje')

def nutricionRedirect(request):
    return redirect301('/servicios/nutricion')

#Redirects a Instructores
def brianRedirect(request):
    return redirect301('/instructores/brian')

def pakoRedirect(request):
    return redirect301('/instructores/pako')

def eduRedirect(request):
    return redirect301('/instructores/edu')

#Redirects a Programas
def boxRedirect(request):
    return redirect301('/programas/box')

def bjjRedirect(request):
    return redirect301('/programas/jiujitsu')

def kidsRedirect(request):
    return redirect301('/programas/kids')

def mmaRedirect(request):
    return redirect301('/programas/artesmarcialesmixtas')

def crossRedirect(request):
    return redirect301('/programas/crossfit')

def sumisionRedirect(request):
    return redirect301('/programas/sumision')

def judoRedirect(request):
    return redirect301('/programas/judo')

#Redes Sociales
def twitter(request):
    return redirect301('http://twitter.com/ffcmexico')

def facebook(request):
    return redirect301('https://www.facebook.com/pages/Fenix-Fight-Club-Mexico/215447585145328?fref=ts')

def youtube(request):
    return redirect('https://www.youtube.com/user/strmrzl')

def foursquare(request):
    return redirect('https://es.foursquare.com/v/fenix-fight-club-m%C3%A9xico/4faeb42ee4b0085e227a6b34')
