import sys
import csv

def main():

    if (len(sys.argv)) < 3:
        sys.exit("Too few command-line arguments")

    elif (len(sys.argv)) > 3:
        sys.exit("Too many command-line arguments")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            with open(sys.argv[2], "w", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["first", "last", "house"]
                )

                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")

                    writer.writerow({
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    })

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

main()
