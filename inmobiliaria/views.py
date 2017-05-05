# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core import serializers
from vinmuebles.models import OfertaDeInmueble, TipoDeOperacion, TipoDeInmueble
from vinmuebles.models import Estado, PrimeraDivisionAdministrativa
import json
import sys
from django.views.decorators.csrf import csrf_exempt


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

def filtros(request):
    template = loader.get_template('filtros.html')
    context = dict()
    return HttpResponse(template.render(context))

def resumen_inmueble(request):
    template = loader.get_template('resumen-inmueble.html')
    context = dict()
    return HttpResponse(template.render(context))

@csrf_exempt
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

	# Si es un post request, entonces se usan filtros de busqueda
	if request.method == 'POST':

		filtros = json.loads(request.body)

		# Se extraen los datos
		antiguedadMax = filtros.get("antiguedadMax", "")
		numeroBanyos = filtros.get("numeroBanyos", "")
		numeroEstacionamientos = filtros.get("numeroEstacionamientos", "")
		numeroHabitaciones = filtros.get("numeroHabitaciones", "")
		operacion = filtros.get("operacion","")
		precioMax = filtros.get("precioMax","")
		tipoDeInmueble = filtros.get("tipoDeInmueble","")

		# Se construye el diccionario de parametros del filter
		filtrosParams = dict()

		if antiguedadMax:
			filtrosParams["antiguedadDeInmueble__lt"] = antiguedadMax

		if numeroBanyos:
			filtrosParams["numeroDeBanyos"] = numeroBanyos

		if numeroEstacionamientos:
			filtrosParams["numeroDeEstacionamientos"] = numeroEstacionamientos

		if numeroHabitaciones:
			filtrosParams["numeroDeHabitaciones"] = numeroHabitaciones

		if operacion:
			tipoDeOperacionID = TipoDeOperacion.objects.filter(nombreDelTipoDeOperacion=operacion)[0]
			filtrosParams["tipoDeOperacion"] = tipoDeOperacionID

		if precioMax:
			filtrosParams["precio__lt"] = precioMax

		if tipoDeInmueble:
			tipoDeInmuebleID = TipoDeInmueble.objects.filter(nombreTipoDeInmueble=tipoDeInmueble)[0]
			filtrosParams["tipoDeInmueble"] = tipoDeInmuebleID

		# Puede ser un post request con filtros vacios
		if filtrosParams:
			todasLasOfertas = OfertaDeInmueble.objects.filter(**filtrosParams)
		else:
			todasLasOfertas = OfertaDeInmueble.objects.all()

	elif request.method == 'GET':
		# No hay filtros
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
	
		estadoID = oferta["fields"]["estado"]
		estado = Estado.objects.filter(id=estadoID)[0]
		oferta["fields"]["estado"] = estado.nombreEstado

		municipioID = oferta["fields"]["municipio"]
		municipio = PrimeraDivisionAdministrativa.objects.filter(id=municipioID)[0]
		oferta["fields"]["municipio"] = municipio.nombreDivision

	datos = json.dumps(datos)

	return HttpResponse(datos, content_type='application/json')