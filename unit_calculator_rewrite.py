def length_calc():
    while True:
        conversion_to_inches = {
            "inches": 1,
            "feet": 12,
            "yards": 36,
            "miles": 63360
        }

        units = list(conversion_to_inches.keys())

        unit_length1 = input(f"Convert from? ({', '.join(units)}): ").lower()
        unit_length2 = input(f"Convert to? ({', '.join(units)}): ").lower()

        if unit_length1 not in conversion_to_inches or unit_length2 not in conversion_to_inches:
            print("Invalid units. Please try again.")

        if unit_length1 == unit_length2:
            print("Units are the same. No conversion needed.")

        try:
            unit_number = float(input(f"How many {unit_length1}? "))
        except ValueError:
            print("Invalid number. Please enter a numeric value.")

        # Convert to inches first, then to target unit
        in_inches = unit_number * conversion_to_inches[unit_length1]
        result = in_inches / conversion_to_inches[unit_length2]

        print(f"{unit_number} {unit_length1} is equal to {result} {unit_length2}.")
        return False


mode = input("What to calculate (length): ").lower()

if mode == "length":
    length_calc()
