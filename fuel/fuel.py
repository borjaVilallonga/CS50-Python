while True:
    try:

        fraction = input("Fraction: ")

        numerador, denominador = fraction.split("/")

        numerador = int(numerador)
        denominador = int(denominador)

        if numerador < 0 or denominador < 0:
            raise ValueError

        if numerador > denominador:
            raise ValueError

        porcentaje = round((numerador / denominador) * 100)


        if porcentaje >= 99:
            print("F")
        elif porcentaje <= 1:
            print("E")
        else:
            print(f"{porcentaje}%")
        break

    except(ValueError, ZeroDivisionError):
        continue
