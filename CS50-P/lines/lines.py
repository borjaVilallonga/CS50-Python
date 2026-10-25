import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count_lines(lines))

def count_lines(lines):
    count = 0

    for line in lines:
        if line.strip() == "":
            continue
        if line.lstrip().startswith("#"):
            continue

        count += 1

    return count

main()
