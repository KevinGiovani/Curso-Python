import time,random, os

from func_terminal import opcion_invalida,clean

def ganador(puntos):
    os.system("cls")
    print("FIN DEL JUEGO")
    if puntos[0] > puntos[1]:
        print("EL GANADOR ES EL JUGADOR", end = " ")
    elif puntos[0] < puntos[1]:
        print("EL GANADOR ES LA MAQUINA", end = " ")
    else:
        print("OCURRIO UN EMPATE", end = " ")
    print(f"({puntos[0]} - {puntos[1]})")

def duelo(jugador, npc, ronda):
    print("\n","PIEDRA!".center(40))
    print("\n","PAPEL!!".center(40))
    print("\n","TIJERA!!!".center(42))
    if jugador==npc:
        print(f"\nHa surgido un empate! ({jugador} - {npc})")
        ganador = None
    elif (jugador=="PAPEL" and npc=="PIEDRA") or (jugador=="TIJERA" and npc=="PAPEL") or (jugador=="PIEDRA" and npc=="TIJERA"):
        print(f"\nEl jugador ha ganado la ronda #{ronda}")
        print(f"{jugador} le gana a {npc}")
        ganador = True
    else:
        print(f"\nLa maquina ha ganado la ronda #{ronda}")
        print(f"{jugador} pierde contra {npc}")
        ganador = False
    input("\nContinuar... ")
    return ganador

def nivel_dificil(jugada):
    pass

    
def nivel_normal(jugada, memoria_npc):
    jugada.extend(memoria_npc) # Si una persona gana, suele repetir el movimiento.
    return random.choice(jugada)

def nivel_facil(jugada):
    return random.choice(jugada)

def pensamiento_maquina(ganador_r):
    match ganador_r:
        case 'PIEDRA':
            return 'PAPEL'
        case 'PAPEL':
            return 'TIJERA'
        case 'TIJERA':
            return 'PIEDRA'

def eleccion_jugador(jugada, ronda, puntos):
    os.system("cls")
    while True:
        print("Ronda #",ronda)
        print(f"JUGADOR: {puntos[0]} - MAQUINA: {puntos[1]}")
        eleccion = input("¿Cual es su elección con la que jugara? (PIEDRA, PAPEL o TIJERA): ")
        if eleccion.upper() in jugada:
            break
        else:
           opcion_invalida()
    return eleccion.upper()
    
def rondas(nivel_npc):
    puntos = [0, 0] # [jugador, npc]
    jugada = ["PIEDRA", "PAPEL", "TIJERA"]
    ronda = 1
    memoria_npc = []
    while ronda <= 3:
        jugador = eleccion_jugador(jugada,ronda, puntos)
        match nivel_npc:
            case "FACIL":
                npc = nivel_facil(jugada)
            case "NORMAL":
                npc = nivel_normal(jugada, memoria_npc)
            case "DIFICIL":
                npc = nivel_dificil(jugada)
        time.sleep(1)
        print("\nLa maquina ya decidio su jugada!...")
        time.sleep(1)
        input("\nPresione una tecla para comenzar el duelo! ")
        resultado = duelo(jugador, npc, ronda)
        if resultado:
            memoria_npc.append(pensamiento_maquina(jugador))
            puntos[0] += 1
        elif resultado is False:
            memoria_npc.append(pensamiento_maquina(npc))
            puntos[1] += 1
        ronda += 1
    ganador(puntos)
    clean()
   
def dificultad():
    opciones = ("FACIL", "NORMAL", "DIFICIL","R")
    while True:
        print("Escoje la dificultad de la maquina:")
        nivel_npc = input("- FACIL\n- NORMAL\n- DIFICIL\nSi desea regresar al menu anterior ingrese 'R'\nOpción: ")
        nivel_npc = nivel_npc.upper()
        if nivel_npc in opciones:
            if(nivel_npc=="DIFICIL"):
                print("\nPROXIMAMENTE...\n")
                clean()
            elif(nivel_npc!="R"):
                rondas(nivel_npc)
            elif(nivel_npc=="R"):
                os.system("cls")
                break
        else:
            opcion_invalida()