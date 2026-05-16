def main():
    time = input("What time is it? ")
    t = convert(time)
    if t >= 7 and t <= 8:
        print("breakfast time")
    elif t >= 12 and t <= 13:
        print("lunch time")
    elif t >= 18 and t <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

main()