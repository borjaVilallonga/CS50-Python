def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False

    if not s[:2].isalpha():
        return False

    numero_encontrado = False

    for letra in s:
        if not letra.isalnum():
            return False

        if letra.isdigit():
            if not numero_encontrado:
                numero_encontrado = True

                if letra == "0":
                    return False

        elif numero_encontrado:
            return False

    return True

main()
