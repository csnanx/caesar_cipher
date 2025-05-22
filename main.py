alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_number):
    encrypted_text = ""
    for char in original_text:
        shifted_char_index = alphabet.index(char) + shift_number
        shifted_char_index = shifted_char_index % len(alphabet)
        shifted_char = alphabet[shifted_char_index]
        encrypted_text += shifted_char

def decrypt(original_text, shift_number):
    decrypted_text = ""
    for char in original_text:
        shifted_char_index = alphabet.index(char) - shift_number
        shifted_char_index = shifted_char_index % len(alphabet)
        shifted_char = alphabet[shifted_char_index]
        decrypted_text += shifted_char
