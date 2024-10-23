def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    return

def encode_pas(password):
    encoded_password = ""
    for chr in password:
        chr = int(chr)
        chr += 3
        chr = str(chr)
        encoded_password += chr
    return encoded_password

def decode_pas(encoded_password):
    decoded_password = ""
    for chr in encoded_password:
        chr = int(chr)
        chr -= 3
        decoded_password += str(chr)
    return decoded_password

def main():
    encoded_pas = None
    new_pass = None
    continue_loop = True

    while continue_loop:
        print_menu()
        user_input = int(input("Please enter an option: "))

        if user_input == 1:
            new_pas = input("Please enter your password to encode: ")
            encoded_pas = encode_pas(new_pas)
            print("Your password has been encoded and stored!")
            print()

        if user_input == 2:
            if encoded_pas:
                decoded_pas = decode_pas(encoded_pas)
                print(f"The encoded password is {encoded_pas}, and the original password is {new_pas}")
            else:
                print("No encoded password found.")
            print()

        if user_input == 3:
            break

if __name__ == "__main__":
    main()
