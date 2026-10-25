# Meter expresion
variable = input("Expression: ")

# Separar cada una de la partes en variables
x, y, z = variable.split()

x = float(x)
z = float(z)

# Operaciones
if y == "+":
    resultado =  x + z
elif y == "-":
    resultado = x - z
elif y == "/" and y != 0:
    resultado = x / z
else:
    resultado = x * z

print(resultado)
