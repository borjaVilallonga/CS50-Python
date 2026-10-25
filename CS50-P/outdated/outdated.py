meses = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:

        fecha = input("Date: ").strip()

        if "/" in fecha:
            mes, dia, año = fecha.split("/")

            mes = int(mes)
            dia = int(dia)
            año = int(año)

        else:
            mes, resto = fecha.split(" ", 1)
            dia, año = resto.split(", ")

            if mes not in meses:
                raise ValueError

            mes = meses.index(mes) +1
            dia = int(dia)
            año = int(año)

        if mes < 1 or mes > 12:
            raise ValueError

        if dia < 1 or dia > 31:
            raise ValueError

        print(f"{año:04}-{mes:02}-{dia:02}")
        break

    except (ValueError, IndexError):
        pass
