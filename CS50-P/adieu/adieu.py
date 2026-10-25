import inflect

p = inflect.engine()

miLista = []

while True:
    try:
        valor = input("Name: ")
        miLista.append(valor)
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(miLista)}")
