resultado = 50

while resultado > 0:
    print (f"Amount Due: {resultado}")

    coin = int(input("Insert Coin: "))

    if coin in (25, 10, 5):
        resultado -= coin

    change_owed = abs(resultado)

    print(f"Change Owed: {change_owed}")
