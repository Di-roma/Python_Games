# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con ____________.

#organizacion = "freeCodeCamp"

#print("Aprende a programar con " + organizacion)
#print("Aprende a programar con {}".format(organizacion))
#print(f"Aprende a programar con {organizacion}") #f-string

# Mad Libs (Hostorias Locas)

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")

madlib = f"¡Progamar es tan {adj}! Siempre me gusta porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)