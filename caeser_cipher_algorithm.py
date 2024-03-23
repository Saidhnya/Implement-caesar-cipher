def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                ascii_offset = ord('a')
            else:
                ascii_offset = ord('A')
            shifted_char = chr((ord(char) - ascii_offset + mode * shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (E/D): ").lower()
        if choice not in ['e', 'd']:
            print("Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'e':
            encrypted_message = caesar_cipher(message, shift, 1)
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = caesar_cipher(message, shift, -1)
            print("Decrypted message:", decrypted_message)
        
        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
