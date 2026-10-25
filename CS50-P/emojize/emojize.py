from emoji import emojize

entrada = input("Input: ")

salida = emojize(entrada, language="alias")

print(f"Output: {salida}")
