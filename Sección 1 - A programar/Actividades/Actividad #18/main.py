"""
Juego Piedra, papel, tijera
Con los conocimientos adquiridos, intenta desarrollar el juego de Piedra, 
papel, tijera
"""
import os
from juego import dificultad
from func_terminal import opcion_invalida, clean

def jugar():
    """
    Limpia el contenido de la terminal y llama la función dificultad()
    del modulo func_terminal
    """
    os.system("cls")
    dificultad()

def reglas():
    """ 
    Muestra las reglas generales sobre como jugar y en que casos se declara
    uno como ganador en las rondas en juego
    """
    print("\n","*"*50)
    print("¿COMO JUGAR?\n- En este juego jugaras contra la maquina, el mejor de 3 rondas sera el ganador")
    print("Recuerda que:"
          "\n1. La tijera gana al papel porque le puede cortar."
          "\n2. La piedra gana a las tijeras porque las rompe."
          "\n3. El papel gana a la piedra porque la envuelve.")
    print("*"*50,"\n")

def menu():
    """
    Menu principal donde el usuario puede escoger entre varias opciones lo que desea
    realizar en la entrada desde la terminal, las opciones disponibles son el jugar, 
    ver las reglas y salir (finalizar el programa)
    """
    while True:
        print("Piedra, papel o tijera")
        opcion = input("Menu:\n- JUGAR\n- REGLAS\n- SALIR\nIngresa una opción: ")
        opcion = opcion.upper()
        match opcion:
            case "JUGAR":
                jugar()
            case "REGLAS":
                reglas()
                clean()
            case "SALIR":
                print("\nGracias por jugar, nos vemos!\n")
                break
            case  _:
                opcion_invalida()

def main():
    """
    Limpia la terminal y llama la función menu()
    """
    os.system("cls")
    menu()
                
main()