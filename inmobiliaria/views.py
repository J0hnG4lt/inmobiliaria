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



def vInmuebles(request, pagina=None) :
	
	if pagina : 
		pagina = int(pagina)
	else :
		pagina = 0

	numeroDeInmueblesPorPagina=9
	cotaInferior = pagina*numeroDeInmueblesPorPagina
	cotaSuperior = (pagina+1)*numeroDeInmueblesPorPagina

	todasLasOfertas = OfertaDeInmueble.objects.all()
	numeroTotalDeOfertas = len(todasLasOfertas)

	if cotaSuperior > numeroTotalDeOfertas :
		cotaSuperior = numeroTotalDeOfertas
		cotaInferior = numeroTotalDeOfertas - numeroDeInmueblesPorPagina

		if cotaInferior < 0 :
			cotaInferior = 0
	
	ofertas = todasLasOfertas[cotaInferior:cotaSuperior]

	datos = serializers.serialize('json', ofertas)
	datos = json.loads(datos)
	for oferta in datos :
		tipoDeInmuebleID = oferta["fields"]["tipoDeInmueble"]
		tipoDeInmueble = TipoDeInmueble.objects.filter(id=tipoDeInmuebleID)[0]
		oferta["fields"]["tipoDeInmueble"] = tipoDeInmueble.nombreTipoDeInmueble

		tipoDeOperacionID = oferta["fields"]["tipoDeOperacion"]
		tipoDeOperacion = TipoDeOperacion.objects.filter(id=tipoDeOperacionID)[0]
		oferta["fields"]["tipoDeOperacion"] = tipoDeOperacion.nombreDelTipoDeOperacion
	
	datos = json.dumps(datos)

	return HttpResponse(datos, content_type='application/json')