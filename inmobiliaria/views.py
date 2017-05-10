# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core import serializers
from vinmuebles.models import OfertaDeInmueble, TipoDeOperacion, TipoDeInmueble
from vinmuebles.models import Estado, PrimeraDivisionAdministrativa, Pais
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


def obtener_paises(request):
	paises = Pais.objects.all()
	datos = serializers.serialize('json', paises)
	datos = json.loads(datos)
	datos = json.dumps(datos)

	return HttpResponse(datos, content_type='application/json')


def obtener_estados(request, pais=None):
	paisID = Pais.objects.filter(nombrePais=pais)
	nombres = []
	if paisID :
		estados = Estado.objects.filter(pais=paisID)
		for estado in estados :
			nombres.append(estado.nombreEstado)

	datos = json.dumps(nombres)
	return HttpResponse(datos, content_type='application/json')

def obtener_municipios(request, pais=None, estado=None):
	paisID = Pais.objects.filter(nombrePais=pais)
	estadoID = Estado.objects.filter(nombreEstado=estado, pais=paisID)
	nombres = []
	if estadoID :
		municipios = PrimeraDivisionAdministrativa.objects.filter(estado=estadoID)
		for municipio in municipios :
			nombres.append(municipio.nombreDivision)

	datos = json.dumps(nombres)
	return HttpResponse(datos, content_type='application/json')

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
		# Estos nombres de los get dependen de los nombres usados en 
		#   filtros.component.ts
		antiguedadMax = filtros.get("antiguedadMax", "")
		metrosCuadradosMin = filtros.get("metrosCuadradosMin", "")
		metrosCuadradosMax = filtros.get("metrosCuadradosMax", "")
		numeroBanyos = filtros.get("numeroBanyos", "")
		numeroEstacionamientos = filtros.get("numeroEstacionamientos", "")
		numeroHabitaciones = filtros.get("numeroHabitaciones", "")
		operacion = filtros.get("operacion","")
		precioMax = filtros.get("precioMax","")
		precioMin = filtros.get("precioMin","")
		pais = filtros.get("pais","")
		estado = filtros.get("estado","")
		municipio = filtros.get("municipio","")
		tipoDeInmueble = filtros.get("tipoDeInmueble","")

		# Se construye el diccionario de parametros del filter
		filtrosParams = dict()

		if antiguedadMax:
			filtrosParams["antiguedadDeInmueble__lt"] = antiguedadMax

		if metrosCuadradosMin:
			filtrosParams["metrosDeConstruccion__gt"] = metrosCuadradosMin

		if metrosCuadradosMax:
			filtrosParams["metrosDeConstruccion__lt"] = metrosCuadradosMax

		if numeroBanyos:
			filtrosParams["numeroDeBanyos"] = numeroBanyos

		if numeroEstacionamientos:
			filtrosParams["numeroDeEstacionamientos"] = numeroEstacionamientos

		if numeroHabitaciones:
			filtrosParams["numeroDeHabitaciones"] = numeroHabitaciones

		if operacion:
			tipoDeOperacionID = TipoDeOperacion.objects.filter(nombreDelTipoDeOperacion=operacion)
			# Por si no existe en el modelo
			if tipoDeOperacionID :
				filtrosParams["tipoDeOperacion"] = tipoDeOperacionID[0]

		if precioMax:
			filtrosParams["precio__lt"] = precioMax

		if precioMin:
			filtrosParams["precio__gt"] = precioMin

		if pais:
			paisID = Pais.objects.filter(nombrePais=pais)
			# Por si no existe en el modelo
			if paisID :
				filtrosParams["pais"] = paisID[0]

		if estado:
			estadoID = Estado.objects.filter(nombreEstado=estado)
			# Por si no existe en el modelo
			if estadoID :
				filtrosParams["estado"] = estadoID[0]

		if municipio:
			municipioID = PrimeraDivisionAdministrativa.objects.filter(nombreDivision=municipio)
			# Por si no existe en el modelo
			if municipioID :
				filtrosParams["municipio"] = municipioID[0]

		if tipoDeInmueble:
			tipoDeInmuebleID = TipoDeInmueble.objects.filter(nombreTipoDeInmueble=tipoDeInmueble)
			# Por si no existe en el modelo
			if tipoDeInmuebleID :
				filtrosParams["tipoDeInmueble"] = tipoDeInmuebleID[0]

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