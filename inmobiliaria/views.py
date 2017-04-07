# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

def index(request):
    template = loader.get_template('index.html')
    context = {
            'latest_question_list': []
        }
    return HttpResponse(template.render(context, request))