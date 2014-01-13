prueba_codetag
==============

Prueba ingreso Certicámara

El presente trabajo se elaboró como prueba para el ingreso a Certicámara.

Lenguaje de Programación: Phyton
Framework: Django
Licencia: Creative Commons
Este ejercicio es un ejemplo de Public Key Cryptography


1.  Se generaron dos llaves ejecutando el comando ssh-keygen.
2.  Para implementar el servicio que registra una llave pública se creó un proyecto de Django llamado "certi" dentro del cual se creó una aplicación llamada "llaves". En el archivo views.py, dentro de la aplicación "llaves" se creó la vista register, lo primero que se hizo fue crear un condicional para identificar si se está realizando un POST o un GET, como se busca realizar un POST para lograr el registro un mensaje de error aparecerá en caso de presentarse un GET.
Luego se crea un bloque try-except para capturar la información del request que viene como un json, se tratan las excepciones y son retornadas según sea el caso como diccionarios json, adicionalmente se creó un modelo sencillo llamado "Llave" para que la llave fuese guardada como string en la base de datos con un id único. 
Para poder saber que la llave fue registrada correctamente se le modificó el status_code para que   retornara el HttpResponse con código 201, también se retorna un json indicando el id correspondiente a la llave registrada. Paralelamente se creó una base de datos en Postgres, un usuario y se garantizaron todos los privilegios.

3.  Para implementar un servicio de validación se requería enviar tres elementos al servidor: 
a. el id de la llave pública que ya esta guardado en el servidor.
b. el mensaje sin encriptar.
c. la firma del mensaje.
Lo primero que se comprueba es que el id exista en la base de datos, por lo tanto que exista la llave pública anteriormente registrada que además es utilizada para verificar la firma.
En una variable se guarda el id obtenido mediante un request.GET, del mismo modo se obtienen los mensajes, el encriptado y el no encriptado, en una variable llamada resultado se guarda el booleano que será True si las llaves son correctas o False si no lo son.
Para verificar la firma se creó una función que recibe como parámetros de entrada la llave pública registrada en el servidor, el mensaje encriptado y el mensaje no encriptado.

4.  Se implemento el comando firma_texto.py dentro de la carpeta "libreria".
Modo de Uso: python firma_texto.py "texto" "ruta/hacia/llave_privada" 
Nota: El comando retorna la firma correspondiente al mensaje codificada para usar en una URL.

5.  El servicio esta publicado en http://peaceful-tundra-4922.herokuapp.com/ los endpoints son:
POST a /register con json {"pub":"llave_publica"}
GET a /validate?id=numero&clearText=mensaje no encriptado&cryptedText=firma del mensaje
