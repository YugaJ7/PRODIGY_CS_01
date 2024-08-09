def caesar_cipher(message, shift, choice ):
    result = ""
    # Adjust shift for decryption
    if choice == "2":  
        shift = -shift
    
    for char in message:  
        if char.isalpha():  # Check if character is a letter  
            shift_base = 65 if char.isupper() else 97  # Base for uppercase or lowercase  
            # Perform the shift and wrap around using modulo  
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)  
        else:  
            result += char  # Non-alphabetic characters remain unchanged  
    
    return result


while True:
        print("Caesar Cipher Program")
        print("---------------------")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice in ["1","2"]:
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            new_message = caesar_cipher(message, shift, choice)
            if choice =="1":
                print(f"Encrypted message: {new_message}")
            else: 
                print(f"Decrypted message: {new_message}")
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
