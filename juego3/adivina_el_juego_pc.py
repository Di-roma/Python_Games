import random


def adivina_el_juego_pc(x):
    print("==========================================")
    print("¡Bienvenido al juego!")
    print("==========================================")
    print(f"Selecciona un número entre 1 y {x} para que el ordenador intente adivinarlo...")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        # Generar predicción del ordenador
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior

        # Obtener respuesta del usuario
        respuesta = input(
            f"¿Mi predicción es {prediccion}? "
            "Si es muy alta ingresa (A), si es muy baja ingresa (B), "
            "si es correcta ingresa (C): "
        ).lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"¡Yay! ¡He adivinado tu número, que es {prediccion}, correctamente!")


adivina_el_juego_pc(10)
