Para hacer uso de la distribución de paquetes de forma correcta:
* Primero: Crear un paquete (en este ejemplo lleva como tal el mismo nombre "paquete" la carpeta usada)
* Segundo: Dentro de paquete crear el archivo "__init__.py" (Este archivo sirve para que Python lo interprete como modulo (paquete) que contiene otros modulos y asi importarlos)
Nota: Este archivo no tiene contenido en la mayoria de los casos.
* Tercero: Dentro de paquete se crea el archivo que se estara usando en la distribución, en este ejemplo solo es uno y se llama "funcion.py"
* Cuarto:  En la raiz del directorio en uso (fuera de la carpeta "paquete") se crea el archivo "setup.py" el cual se configurara
  para crear el modulo en cuestion. En este se menciona información como nombre del paquete, versión, descripción, entre otros datos.
* Quinta: Ejecutar el archivo setup desde la terminal: "py setup.py sdist". Una vez ejecutado el comando, si todos los pasos fueron hechos correctamente,
 se creara en la raiz dos carpetas llamado "dist" y otro con terminación "*.egg-info".
* Sexto: Para hacer uso ahora del paquete de distribución nos dirigimos desde la terminal a la carpeta "dist" y encontraremos el archivo compromido en
  formato ".tar.gz". Posteriormente procedemos a instalar con el comando "pip install nombre-del-paquete" (en este caso el nombre del paquete generado es
  paquete-0.1.tar.gz) Nota: para realizar la desinstalación se ingresa en la terminal "pip uninstall nombre" (esta vez sin especificar formato)
* Septimo: Para comprobar el uso del paquete distribuible con correcto funcionamiento se hace uso del archivo que se encuentra en la raiz de la carpeta "Sección 1 - A programar" llamado: "clase17_ejemplo-paquete_distribuible"

* Para ver los paquetes instalados usar el comando "pip list" y para ver mas información de un paquete en especifico usar el comando "pip show nombre-del-paquete"

Nota: El archivo de "clase17_paquetes_import", en este solo se estan realizando las importaciones de una forma directa, este servio de ejemplo antes de saber usar la distribución y sobre todo el cuando hacer uso de este.