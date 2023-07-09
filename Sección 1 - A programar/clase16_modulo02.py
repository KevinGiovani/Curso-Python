from random import randint as azar # azar es el alias
# from random import * - (Importamos todas las funciones de random)

continua = "S"
while (continua=="S"):
    lanzaDado = azar(1,6) # Numero azar entre 1 y 6
    print(f"\nHaz obtenido un {lanzaDado}")
    continua = input("\n¿Deseas continuar? (S/N): ").upper()

print("\nYa no se lanzara el dado, ADIOS!\n")