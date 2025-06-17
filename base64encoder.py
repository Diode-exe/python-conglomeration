import base64

mode = input("1 for encode, 2 for decode: ")

if mode == "1":
    while True:
        to_encode = input("String to encode: ")

        encoded = base64.b64encode(to_encode.encode())

        print(f"Output: {encoded}")

        save_to_file = input("Save to file? y or n: ").lower().strip()
        if save_to_file == "y".lower():
            with open ("b64_encode_results.txt", "a") as file:
                file.write(f"Input: {to_encode}")
                file.write(f"Output: {encoded}\n")
                file.write("-" * 30 + "\n")
            print("Saved to b64_encode_results.txt")
        else:
            print("Not saving.")
elif mode == "2":
    while True:
        to_decode = input("String to decode: ")

        decoded = base64.b64decode(to_decode).decode()

        print(f"Output: {decoded}")

        save_to_file = input("Save to file? y or n: ").lower().strip()
        if save_to_file == "y".lower():
            with open ("b64_decode_results.txt", "a") as file:
                file.write(f"Input: {to_decode}")
                file.write(f"Output: {decoded}\n")
                file.write("-" * 30 + "\n")
            print("Saved to b64_decode_results.txt")
        else:
            print("Not saving.")
else:
    print("Invalid mode. ")