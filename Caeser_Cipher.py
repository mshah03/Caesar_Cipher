def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shift_amount = shift % 26  # Ensure shift stays within 26 characters
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                encrypted_text += chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            encrypted_text += char  # If character is not alphabet, keep it as it is
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift) # -shift will reverse the shift for decryption 

choice = input("Enter 'E' for encryption and 'D' for decryption: ").upper()
if choice=='E':
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift key (an integer): "))
    encrypted_text = caesar_cipher_encrypt(text, shift)
    print("Encrypted text: ", encrypted_text)
elif choice=='D':
    text = input("Enter the text to decrypt: ")
    shift = int(input("Enter the shift key (an integer): "))
    decrypted_text = caesar_cipher_decrypt(text, shift)
    print("Decrypted text: ", decrypted_text)


