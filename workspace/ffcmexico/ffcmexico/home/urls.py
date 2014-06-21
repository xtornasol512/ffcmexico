from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView


urlpatterns=patterns('ffcmexico.home.views',
    #HOME
	url(r'^$','index_view', name='vista_principal'),
    #estaticos
	url(r'^humans.txt$', TemplateView.as_view(template_name='home/humans.txt', content_type='text/plain; charset=utf-8')),
	url(r'^robots.txt$', TemplateView.as_view(template_name='home/robots.txt', content_type='text/plain; charset=utf-8')),
    url(r'^sitemap.xml$', TemplateView.as_view(template_name='home/sitemap.xml', content_type='application/xml; charset=utf-8')),
    #Programas
    url(r'^programas$', 'programas'),
    url(r'^programas/jiujitsu$', 'bjj'),
    url(r'^programas/kids$', 'kids'),
    url(r'^programas/box$', 'box'),
    url(r'^programas/crossfit$', 'cross'),
    url(r'^programas/judo$', 'judo'),
    url(r'^programas/sumision$', 'sumision'),
    url(r'^programas/artesmarcialesmixtas$', 'mma'),
    #redirects de programas
    url(r'^bjj$', 'bjjRedirect'),
    url(r'^brazilianjiujitsu$', 'bjjRedirect'),
    url(r'^jiujitsu$', 'bjjRedirect'),
    url(r'^judo$', 'judoRedirect'),
    url(r'^mma$', 'mmaRedirect'),
    url(r'^ufc$', 'mmaRedirect'),
    url(r'^sumision$', 'sumisionredirect'),
    url(r'^submission$', 'sumisionredirect'),
    url(r'^mixedmartialarts$', 'mmaRedirect'),
    url(r'^artesmarcialesmixtas$', 'mmaRedirect'),
    url(r'^cross$', 'crossRedirect'),
    url(r'^crossfit$', 'crossRedirect'),
    url(r'^box$', 'boxRedirect'),
    url(r'^boxing$', 'boxRedirect'),
    url(r'^kids$', 'kidsRedirect'),
    url(r'^ninos$', 'kidsRedirect'),
    #Instructores
    url(r'^instructores/$', 'instructores'),
    url(r'^instructores/brian$', 'brian'),
    url(r'^instructores/pako$', 'pako'),
    url(r'^instructores/edu$', 'edu'),
    #Redirects de Instructores
    url(r'^brian/$', 'brianRedirect'),
    url(r'^boss/$', 'brianRedirect'),
    url(r'^pako/$', 'pakoRedirect'),
    url(r'^paco/$', 'pakoRedirect'),
    url(r'^edu/$', 'eduRedirect'),
    #Servicios
    url(r'^servicios/$', 'servicios'),
    url(r'^servicios/fisioterapia$', 'terapia'),
    url(r'^servicios/masaje$', 'masaje'),
    url(r'^servicios/nutricion$', 'nutricion'),
    #redirects Servicios
    url(r'^terapia$', 'terapiaRedirect'),
    url(r'^fisioterapia$', 'terapiaRedirect'),
    url(r'^fisioterapeuta$', 'terapiaRedirect'),
    url(r'^terapeuta$', 'terapiaRedirect'),
    url(r'^miguel$', 'terapiaRedirect'),
    url(r'^masaje$', 'masajeRedirect'),
    url(r'^estrellita$', 'masajeRedirect'),
    url(r'^estrella$', 'masajeRedirect'),
    url(r'^nutricion$', 'nutricionRedirect'),
    #Galerias
    url(r'^galeria$', 'galeria'),
    url(r'^galeria/fotos$', 'fotos'),
    url(r'^galeria/videos$', 'videos'),
    #redirects Galerias
    url(r'^galerias$', 'galeriaRedirect'),
    url(r'^videos$', 'videosRedirect'),
    url(r'^fotos$', 'fotosRedirect'),
    #Paginas Privacidad
    url(r'^privacidad/terminosycondiciones$', 'terminos'),
    #Redirects Privacidad
    url(r'^privacidad$', 'terminosRedirect'),
    url(r'^terminos$', 'terminosRedirect'),
    url(r'^condiciones$', 'terminosRedirect'),
    #Paginas HOME
    url(r'^about$', 'nosotros'),
    url(r'^horario$', 'horario'),
    url(r'^contacto$', 'contacto'),
    url(r'^codigo$', 'codigoconducta'),
    url(r'^freeweek$', 'freeweek'),
    url(r'^semanagratis$', 'freeweek'),
    url(r'^mapa$', 'maps'),
    url(r'^faqs$', 'faqs'),
    url(r'^sink$', 'sink'),


    #Enlaces Externos
    url(r'^twitter$', 'twitter'),
    url(r'^facebook$', 'facebook'),
    url(r'^youtube$', 'youtube'),
    url(r'^4square$', 'foursquare'),
    url(r'^foursquare$', 'foursquare'),



)