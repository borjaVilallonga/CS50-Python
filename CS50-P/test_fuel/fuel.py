def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    try:
        numerador, denominador = fraction.split("/")

        numerador = int(numerador)
        denominador = int(denominador)

        if numerador < 0 or denominador < 0:
            raise ValueError

        if denominador == 0:
            raise ZeroDivisionError

        if numerador > denominador:
            raise ValueError

        porcentaje = round((numerador / denominador) * 100)

        return porcentaje

    except ZeroDivisionError:
        raise


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
