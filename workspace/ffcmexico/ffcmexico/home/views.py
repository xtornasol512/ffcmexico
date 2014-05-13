# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def index_view(request):
	return render_to_response('home/index.html',{'hola':"fatima"},context_instance=RequestContext(request))

def humans(request):
	return render_to_response('home/humans.txt',{'hola':"fatima"},context_instance=RequestContext(request))

def robots(request):
	return render_to_response('home/robots.txt',{'hola':"fatima"},context_instance=RequestContext(request))