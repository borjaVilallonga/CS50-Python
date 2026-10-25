import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"
    matches = re.search(pattern, s)

    if not matches:
        raise ValueError

    hour1 = int(matches.group(1))
    minute1= int(matches.group(2) or 0)
    period1 = matches.group(3)

    hour2 = int(matches.group(4))
    minute2= int(matches.group(5) or 0)
    period2 = matches.group(6)

    if hour1 < 1 or hour1 >12 or hour2 < 1 or hour2 > 12:
        raise ValueError

    if minute1 > 59 or minute2 > 59:
        raise ValueError

    if period1 == "AM" and hour1 == 12:
        hour1 = 0
    elif period1 == "PM" and hour1 != 12:
        hour1 += 12

    if period2 == "AM" and hour2 == 12:
        hour2 = 0
    elif period2 == "PM" and hour2 != 12:
        hour2 += 12

    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"


if __name__ == "__main__":
    main()
