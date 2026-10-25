from datetime import date
import sys
import inflect

def main():
    fecha = input("Date of Birth: ")
    try:
        fecha = date.fromisoformat(fecha)
    except ValueError:
        sys.exit("Invalid date")

    print(minutes_since_birth(fecha))


def minutes_since_birth(fecha):

    hoy = date.today()
    dias = (hoy - fecha).days
    minutos = dias * 24 * 60

    p = inflect.engine()
    return p.number_to_words(minutos, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()
