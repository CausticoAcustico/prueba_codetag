from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from models import Llave
from django.utils import simplejson
from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256 
from base64 import b64decode 

def home(request):
    return render(request, 'llaves/hola_mundo.html', {})


@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            data = simplejson.loads(request.body)
        except:
            return HttpResponseBadRequest(simplejson.dumps({'error': 'no es un json'}))
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

@csrf_exempt
def validate(request):
    id_recibido = request.GET['id']
    try:
        key = Llave.objects.get(id=id_recibido)
    except:
        return HttpResponseBadRequest(simplejson.dumps({'error':'El id solicitado no existe'}))

    texto_encriptado = request.GET['cryptedText']
    texto = request.GET['clearText']

    resultado = verify_sign(key.llave,texto_encriptado,texto)
    if resultado:
        return HttpResponse(simplejson.dumps({'OK': 'Las llaves son correctas'}))
    else:
        return HttpResponseBadRequest(simplejson.dumps({'error':'Las firmas no coinciden'}))

    return HttpResponse('No se aceptan Post')

def verify_sign(pub_key, signature, data):
    rsakey = RSA.importKey(pub_key) 
    signer = PKCS1_v1_5.new(rsakey) 
    digest = SHA256.new() 
    digest.update(data.encode("utf-8","ignore")) 
    if signer.verify(digest, b64decode(signature)):
        return True
    return False
