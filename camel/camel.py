# Tomar el entrada de string
camelCase = input("camelCase: ")

# Variabel vacia resultado
resultado = ""

# Recorrer entrada letra a letra y añadir _ cuando aparezca la mayuscula y ponerlo la minuscula
for letra in camelCase:
    if letra.isupper():
        resultado += "_" + letra.lower()
    else:
        resultado += letra

print(f"snake_case: {resultado}")
