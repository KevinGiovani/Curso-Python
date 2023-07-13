Esta clase para hacerla mas practica y comprensible se crearon 2 subcarpetas para demostrar el funcionamiento
de la reinstalación de librerias en diferentes entornos virtuales.
* Parte 1 (Carpeta):
Dentro de esta primera carpeta se creara un entorno virtual, para ello se utiliza el siguiente comando:
"py -m venv venv" y para activar el entorno se utiliza el comando "venv/Scripts/activate". Una vez activado
instalamos diferentes librerias con el comando pip, como por ejemplo "pip install pandas" y "pip install matplotlib".
Para mostrar todos las librerias que han sido instalados por el usuario se utiliza el comando "pip freeze", este ademas
muestras el numero de versión de cada libreria que esta en uso.

Ahora, para instalar todos los librerias que se estan utilizando en este proyecto en mas proyectos es necesario utilizar
un archivo de texto, es por ello que se tendra que utilizar el comando "pip freeze > requeriments.txt". Basicmente lo que
realiza el anterior comando es que pasa el contenido que devuelve "pip freeze" a un archivo de texto el cual se le dio
de nombre como "requeriments.txt".

Nota: Para continuar con la siguiente parte no olvidar desactivar el entorno virtual actual usando el comando "deactivate".

* Parte 2 (Carpeta):
Simulando de que esta carpeta se trata de otro nuevo proyecto en el cual necesitamos utilizar las librerias instaladas
en el proyecto anterior (Parte 1). Primero procederemos a copiar el archivo "requirements.txt" del proyecto anterior y lo
pasaremos a este. Ahora, nuevamente creamos otro entorno virtual y lo activamos. Finalmente para instalar las librerias
que incluye el archivo "requirements.txt" utilizamos el comando "pip install -r requirements.txt". Utilizando el comando
"pip freeze" podemos observar que las librerias que teniamos instaladas en el primer entorno virtual tambien estaran ahora
en este segundo entorno virtual.
