import random

def jugar():
    usuario = input("Elige una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera. \n ").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return "¡Es un empate!"
    if es_ganador(usuario, computadora):
        return "¡Ganaste!"
    return "¡Perdiste!"

def es_ganador(jugador, oponente):
    # Devuelve True si el jugador gana
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())