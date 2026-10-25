def main():
    texto = input("Input: ")
    print(shorten(texto))


def shorten(word):
    resultado = ""

    for letra in word:
        if letra.lower() not in ("a", "e", "i", "o", "u"):
            resultado += letra

    return resultado


if __name__ == "__main__":
    main()
