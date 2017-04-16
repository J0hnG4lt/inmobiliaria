# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core import serializers
from vinmuebles.models import OfertaDeInmueble

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

	numeroDeInmueblesPorPagina=10
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
	
	return HttpResponse(datos, content_type='application/json')