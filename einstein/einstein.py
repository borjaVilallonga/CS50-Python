# input de mass
mass = int(input("mass:"))

# function einstein
def einstein():
    c = 300000000
    e = mass * c**2
    return e

# function main
def main():
    print(einstein())

main()
