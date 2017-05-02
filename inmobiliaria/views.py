# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core import serializers
from vinmuebles.models import OfertaDeInmueble, TipoDeOperacion, TipoDeInmueble
import json

def index(request):
    template = loader.get_template('index.html')
    context = {
            'latest_question_list': []
        }
    return HttpResponse(template.render(context, request))

def grid_inmuebles(request):
    template = loader.get_template('grid-inmuebles.html')
    context = dict()
    return HttpResponse(template.render(context))

def resumen_inmueble(request):
    template = loader.get_template('resumen-inmueble.html')
    context = dict()
    return HttpResponse(template.render(context))

def vInmuebles(request, pagina=None) :
	
	# Saneamos el input
	if pagina : 
		pagina = int(pagina)
	else :
		pagina = 0

	# Configuracion
	numeroDeInmueblesPorPagina=9
	cotaInferior = pagina*numeroDeInmueblesPorPagina
	cotaSuperior = (pagina+1)*numeroDeInmueblesPorPagina

	todasLasOfertas = OfertaDeInmueble.objects.all()
	numeroTotalDeOfertas = len(todasLasOfertas)

	# Si solicita pagina que no existe devuelve lista vacia
	if cotaInferior > numeroTotalDeOfertas :
		return HttpResponse(json.dumps([{u'aunFaltanPaginas':False}]),
							content_type='application/json')

	# Si solicita ultima pagina entonces ajusta numero de elementos
	if cotaSuperior > numeroTotalDeOfertas :
		cotaSuperior = numeroTotalDeOfertas
		#cotaInferior = numeroTotalDeOfertas - numeroDeInmueblesPorPagina

		if cotaInferior < 0 :
			cotaInferior = 0

	ofertas = todasLasOfertas[cotaInferior:cotaSuperior]

	# Obtiene el json a partir del modelo de la base de datos
	datos = serializers.serialize('json', ofertas)
	datos = json.loads(datos)

	# Le digo al cliente que esta es la ultima pagina
	datos.append({u'aunFaltanPaginas':cotaSuperior < numeroTotalDeOfertas})

	# Obtiene los objetos de tipo foreign key que se van a usar
	for oferta in datos[:-1] :
		tipoDeInmuebleID = oferta["fields"]["tipoDeInmueble"]
		tipoDeInmueble = TipoDeInmueble.objects.filter(id=tipoDeInmuebleID)[0]
		oferta["fields"]["tipoDeInmueble"] = tipoDeInmueble.nombreTipoDeInmueble

		tipoDeOperacionID = oferta["fields"]["tipoDeOperacion"]
		tipoDeOperacion = TipoDeOperacion.objects.filter(id=tipoDeOperacionID)[0]
		oferta["fields"]["tipoDeOperacion"] = tipoDeOperacion.nombreDelTipoDeOperacion
	
	datos = json.dumps(datos)

	return HttpResponse(datos, content_type='application/json')