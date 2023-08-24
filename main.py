highway_number = int(input("enter highway number: "))


if highway_number >= 1 and highway_number <= 99:
    if highway_number % 2 == 0:
        direction = "east/west"
        print(f"I-{highway_number} is primary, going east/west.")
    else:
        direction = "north/south"
        print(f"I-{highway_number} is primary, going {direction}.")
elif highway_number >= 100 and highway_number <= 999:
    primary_highway = highway_number % 100
    if primary_highway == 0:
        print(f"{highway_number} is not a valid interstate highway number.")
    if primary_highway % 2 == 0:
        direction = "east/west"
        if highway_number != 200:
            print(
                f"I-{highway_number} is auxiliary, serving I-90, going {direction}.")
    else:
        direction = "north/south"
        print(
            f"I-{highway_number} is auxiliary, serving I-5, going {direction}.")
else:
    print(f"{highway_number} is not a valid interstate highway number.")