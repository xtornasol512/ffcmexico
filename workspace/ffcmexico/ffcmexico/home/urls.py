from django.conf.urls import patterns, url, include

urlpatterns=patterns('ffcmexico.home.views',
	url(r'^$','index_view', name='vista_principal'),
	url(r'^humans.txt$', 'humans'),
	url(r'^robots.txt$', 'robots'),
)