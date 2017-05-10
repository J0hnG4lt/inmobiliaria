"""inmobiliaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vinmuebles/(?P<pagina>\d+)', views.vInmuebles),
    url(r'^$', views.index, name="index"),
    url(r'^grid_inmuebles', views.grid_inmuebles, name="grid_inmuebles"),
    url(r'^vinmuebles/obtener_paises', views.obtener_paises, name="obtener_paises"),
    url(r'^vinmuebles/obtener_estados/(?P<pais>\w+)', views.obtener_estados, name="obtener_estados"),
    url(r'^vinmuebles/obtener_municipios/(?P<pais>\w+)/(?P<estado>\w+)/$', views.obtener_municipios, name="obtener_municipios"),
    url(r'^filtros', views.filtros, name="filtros"),
    url(r'^resumen_inmueble', views.resumen_inmueble, name="resumen_inmueble")   
]

urlpatterns += staticfiles_urlpatterns()