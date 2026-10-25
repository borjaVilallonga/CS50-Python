menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

contador = 0


while True:
    try:
        plato = input("Item: ").title()

        if plato in menu:
            contador += menu[plato]
            print(f"Total: ${contador:.2f}")

    except EOFError:
        print()
        break

