# introducir un valor
value = input("What is the Answe to the Great Question of Life, the Universe, and Everything?")

value = value.strip().lower().replace("-", " ")

# Poner las condiciones
match value:
    case "42" | "forty-two" | "forty two" :
        print("Yes")
    case _:
        print("No")
