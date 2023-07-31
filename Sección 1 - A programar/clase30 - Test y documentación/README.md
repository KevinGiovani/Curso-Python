* Docstring:
Documentación de codigo con respecto a funciones, metodos, clases, modulos o paquetes, para ello se utilizan
triple comillas simples o triple comilla doble. La utilidad de esta es que se puede saber mas información sobre
lo que se esta realizando utilizando la función help desde la terminal dentro de python.

Ejemplo (desde la terminal):
1. Ingresamos el comando "py" o "python".
2. Importamos el modulo al cual planteamos consultar su documentación, en este caso el comando es el sig.
 "import clase30_test".
3.  Para realizar la consulta se utiliza la función help(): Sobre la consulta completa del modulo
en este caso no se especifica nada mas que el propio modulo "help(clase30_test)" pero en caso de realizar una 
busqueda determinada bastara con agregar el metodo/función "help(clase30_test.multiplicar)".

* Doctest: Los casos de prueba son definidos dentro del docstring, para ello se define la sentencia de prueba con tres
simbolos de mayor que y posteriormente su sentencia, ejemplo ">>> multiplicar(2, 3)" y seguido en la siguiente linea con su 
respectivo resultado esperado que en este caso es "6". Para comprobar el funcionamiento de las pruebas se usa la terminal con
el siguiente comando  "py -m doctest nombre-modulo" o en este caso "py -m doctest clase30_test.py". En caso de que exista
algun tipo de error este sera mostrado remarcando el caso de prueba que fallo, el valor que se esperaba y el resultado que en realidad
se obtuvo.


Mas información:
  - Pruebas: https://realpython.com/python-doctest/
  - Documentación y pruebas: https://pywombat.com/articles/docstring-python
