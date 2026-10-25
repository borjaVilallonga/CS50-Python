# input para meter el dato
fr = input("Greeting: ")

# limpiar el dato que entra
fr = fr.strip().lower().replace("-", " ")

# poner condicion
if fr.startswith("hello"):
    print("$0")
elif fr.startswith("h"):
    print("$20")
else:
    print("$100")
