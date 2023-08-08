import time,random, os

from func_terminal import opcion_invalida,clean

def ganador(puntos):
    """
    Muestra en la terminal el ganador de las rondas con sus 
    respectivos puntos generados al finalizar el juego

    Args:
        puntos (list): Puntos del usuario y de la maquina
    """
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
    """
    Se establece y muestra en la terminal quien es el ganador de la ronda
    jugada y que tipo de movimientos fueron realizados por ambas partes.

    Args:
        jugador (str): Movimiento realizado del jugador
        npc (str): Movimiento realizado por la maquina
        ronda (int): Ronda en juego (actual)

    Returns:
        bool: Establece el ganador de la ronda
    """
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
    """
    Codigo pendiente a implementar

    Args:
        jugada (list): Movimientos disponibles para realizar
    """
    pass

def nivel_normal(jugada, memoria_npc):
    """
    En esta dificultad se establece a partir del hecho de que la mayoria de los 
    usuarios al jugar se plantean el repetir la misma jugada ganadora para volver
    a ganar. Sabiendo lo anterior, usando la función pensamiento_maquina(ganador_r)
    de forma indirecta se obtiene el resultado que permita ganar a lo dicho anteriormente,
    pero dado a que se trata de aleatoriedad los movimientos se agregan a memoria_npc
    para que se tenga mas posibilidades de que se pueda escoger dicha probabilidad.

    Args:
        jugada (list): Movimientos disponibles para realizar
        memoria_npc (list): Movimientos con los que la maquina  tiene mas posibilidades de 
        ganar dadas victorias realizadas en las rondas anteriores
    Returns:
        str: Movimiento de la maquina
    """
    jugada.extend(memoria_npc) # Si una persona gana, suele repetir el movimiento.
    return random.choice(jugada)

def nivel_facil(jugada):
    """
    Establece de forma aleatoria la elección de la maquina
    sobre el movimiento que realizara en la ronda
    
    Args:
        jugada (list): Movimientos disponibles para realizar

    Returns:
        str : Movimiento de la maquina
    """
    return random.choice(jugada)

def pensamiento_maquina(ganador_r):
    """
    Establece el resultado con el cual la maquina tuviera mas posibilidades de ganar
    en caso de que el jugador se planteara repetir el movimiento ganador de rondas
    anteriores

    Args:
        ganador_r (list): Movimiento(s) con el cual se ganó la ronda

    Returns:
        str: Movimiento con el que gana a ganador_r
    """
    match ganador_r:
        case 'PIEDRA':
            return 'PAPEL'
        case 'PAPEL':
            return 'TIJERA'
        case 'TIJERA':
            return 'PIEDRA'

def eleccion_jugador(jugada, ronda, puntos):
    """
    Elección de movimiento por parte del usuario para realizar
    en contra de la maquina

    Args:
        jugada (list): Movimientos disponibles para realizar
        ronda (int): Estado de encuentro contra la maquina
        puntos (list): Puntos del usuario y de la maquina

    Returns:
        str : Movimiento a realizar del usuario
    """
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
    """
    Rondas en juego en las que se basara para definir el ganador 
    (función ganador(puntos)), en esta el usuario y la maquina 
    escogera su representación en texto del movimiento que realizaran
    a partir de las funciones eleccion_jugador(jugada, ronda, puntos) y segun
    la dificultad de la maquina escogida nivel_x(x), posteriormente
    se estable el ganador de la ronda (función duelo()). La función 
    pensamiento_maquina(x) solo representa su uso actualmente en la 
    dificultad normal ya que se considera como una mejora a la de facil.
    
    Args:
        nivel_npc (str): Dificultad de la maquina
    """
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
            puntos[0] += 1
            if nivel_npc=="NORMAL":
               memoria_npc.append(pensamiento_maquina(jugador))
        elif resultado is False:
            puntos[1] += 1
            if nivel_npc=="NORMAL":
                memoria_npc.append(pensamiento_maquina(npc))
        ronda += 1
    ganador(puntos)
    clean()
   
def dificultad():
    """
    Permite que el usuario escoja la dificultad de la maquina contra la que jugara o si
    lo desea, volver a regresar al menu anterior (función menu() del modulo main).
    Se realizan llamados de funciones como clean() y opción_invalida() del modulo func_terminal
    y el llamado de la función rondas(niveles_npc) de este modulo.
    """
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