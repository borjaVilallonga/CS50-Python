import random

# Bucle para hacer que nivel sea un int de un numero entero (int)
while True:
    try:
        nivel = int(input("Level: "))
        if nivel > 0:
            break
    except ValueError:
        pass

#Generar numero aleatorio
numero = random.randint(1, nivel)

#Aplicar logica del juego
while True:
    try:
        intento = int(input("Guess: "))

        if intento <= 0:
            continue

        if intento < numero:
            print("Too small!")
        elif intento > numero:
            print("Too large!")
        else:
            print("Just right!")
            break

    except ValueError:
        pass
