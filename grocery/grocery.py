listaCompra = {}

while True:
    try:
        item = input().upper()

        if item in listaCompra:
            listaCompra[item] += 1
        else:
            listaCompra[item] = 1

    except EOFError:
        print()
        break

for item in sorted(listaCompra):
    print(listaCompra[item], item)
