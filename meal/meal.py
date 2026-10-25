def main():
    time = input ("Whay time it is?")

    current_time = convert(time)

    if 7 <= current_time <= 8:
        print("breakfast time")
    elif 12 <= current_time <= 13:
        print("lunch time")
    elif 18 <= current_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60



if __name__ == "__main__":
    main()
