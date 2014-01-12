from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from models import Llave
from django.utils import simplejson
# Create your views here.
def home(request):
	return render(request, 'llaves/hola_mundo.html', {})


@csrf_exempt
def register(request):
	if request.method == "POST":
		try:
			data = simplejson.loads(request.body)
		except:
			return HttpResponseBadRequest(simplejson.dumps({'error': 'no es json'}))
		if not data.get('pub'):
			return HttpResponseBadRequest(simplejson.dumps({'error':'json no contiene llave publica'}) )
		llave = data['pub']
		if  Llave.objects.filter(llave = llave):
			return HttpResponseBadRequest(simplejson.dumps({'error': 'la llave ya existe'}))
		
		k = Llave(llave = llave)
		k.save()
		
		response = HttpResponse(simplejson.dumps({"id":k.id}))
		response.status_code = 201 
		return response	

	return HttpResponse('ERROR No se aceptan GETs')
	# return render(request, 'llaves/hola_mundo.html', {})