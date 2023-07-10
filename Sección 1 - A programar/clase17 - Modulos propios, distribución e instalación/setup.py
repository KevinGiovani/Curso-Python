from setuptools import find_packages, setup

VERSION = "0.1"
DESCRIPTION = "Realización de suma de dos valores y comprobación de par/impar"

# Configuración
setup(
    name = "paquete", # El nombre debe coincidir con el nombre de la carpeta
    version = VERSION,
    description = DESCRIPTION,
    author = "Kevin Giovani",
    author_email = "kevingiovani920@outlook.com",
    package = find_packages()
)

# Mas información:
# https://www.freecodecamp.org/espanol/news/como-construir-tu-primer-paquete-de-python/
# https://docs.hektorprofe.net/python/modulos-y-paquetes/paquetes/