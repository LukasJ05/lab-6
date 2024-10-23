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

continue_loop = True
def main():
    while continue_loop:
        print_menu()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            new_pas = input("Please enter your password to encode: ")
            encoded_pas = encode_pas(new_pas)
            print("Your password has been encoded and stored!")
            print()
        if user_input == 2:
            print(f"The encoded password is {encoded_pas}, and the original password is {new_pas}")
            print()
        if user_input == 3:
            break

if __name__ == "__main__":
    main()
