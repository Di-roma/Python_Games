import random


def adivina_el_numero(x):

    print("==========================================")
    print("¡Bienvenido al juego de Adivina el Número!")
    print("==========================================")
    print("Tu meta es adivinar el número generado por el ordenador.")

    numero_aleatorio = random.randint(1, x) #Número aleatorio entre 1 y x

    prediccion = 0

    while prediccion != numero_aleatorio:
        #El usuario inserta un número
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("Intenta de nuevo. El número es muy bajo.")
        elif prediccion > numero_aleatorio:
            print("Intenta de nuevo. El número es muy alto.")

    print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} correctamente.")


adivina_el_numero(10)