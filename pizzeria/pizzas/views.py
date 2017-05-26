from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from pizzas.models import Pizza
from django.http import Http404

# Create your views here.

def index(request):
    pizza_list = Pizza.objects.all()
    #html = ''
    #for pizza in pizza_list:
    #    url = '/pizzas/' + str(pizza.id) + '/'
    #    html += '<a href="' + url + '">' + pizza.name + '</a><br>'
    template = loader.get_template('pizza/index.html')
    context = {
        'pizza_list': pizza_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, pizza_id):
    try:
        pizza = Pizza.objects.get(pk=pizza_id)
    except Pizza.DoesNotExist:
        raise Http404("Esta Pizza no existe")
    return render(request, 'pizza/detail.html', {'pizza': pizza})

def conocenos(request):
    return HttpResponse("<h1>Página Conócenos</h1><h3>Esta es nuestra pizzeria</h3>")

def fichero(request):
    template = loader.get_template('pizza/fichero.html')
    context = {}
    return HttpResponse(template.render(context, request))