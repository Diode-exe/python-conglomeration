def length_calc():
    unit_length1 = input("Convert from?\n" \
    "feet\n" \
    "inches\n" \
    "yards\n" \
    "miles: " \
    "").lower()
    unit_length2 = input("Convert to?\n" \
    "feet\n" \
    "inches\n" \
    "yards\n" \
    "miles: " \
    "").lower()

    unit_number = int(input(f"How many {unit_length1}? "))

    if unit_length1 == unit_length2:
        print(f"{unit_length1} is equal to {unit_length2}, therefore they cannot be converted.")
        print("Running again...")
        length_calc()
    if unit_length1 == "feet" and unit_length2 == "inches":
        result = unit_number / 12
        print(f"{unit_number} {unit_length1} to {unit_length2} equals {result}")
    if unit_length1 == "feet" and unit_length2 == "yards":
        result = unit_number / 3
        print(f"{unit_number} {unit_length1} to {unit_length2} equals {result}")
    if unit_length1 == "feet" and unit_length2 == "miles":
        result = unit_number / 5280
        print(f"{unit_number} {unit_length1} to {unit_length2} equals {result}")
    if unit_length1 == "inches" and unit_length2 == "feet":
        result = unit_number * 12
        print(f"{unit_number} {unit_length1} to {unit_length2} equals {result}")
    if unit_length1 == "inches" and unit_length2 == "yards":
        result = unit_number * 3
        print(f"{unit_number} {unit_length1} to {unit_length2} equals {result}")
    if unit_length1 == "inches" and unit_length2 == "miles":
        result = unit_number * 5280

mode = input("What to calculate\n" \
"length: ").lower()

if mode == "length":
    length_calc()
