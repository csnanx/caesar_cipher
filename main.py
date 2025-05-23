from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "2":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    if encode_or_decode == "1":
        print(f"Here is the encoded result: {output_text}")
    elif encode_or_decode == "2":
        print(f"Here is the decoded result: {output_text}")

def brute_force_decode(original_text):
    for shift_amount in range(1, 26):
        decoded_text = ""
        for letter in original_text:
            if letter in alphabet:
                shifted_index = alphabet.index(letter) - shift_amount
                shifted_letter = alphabet[shifted_index]
                decoded_text += shifted_letter
            else:
                decoded_text += letter
        print(f"shift amount: {shift_amount}\ndecoded text: {decoded_text}\n")

while True:
    direction = input("\nWhat would you like to do?\n1. Encode a message\n2. Decode a message\n3. Brute force a message\n4. Exit\nEnter your choice: ").lower()
    text = input("Type your message:\n").lower()
    if direction == "3":
        brute_force_decode(text)
    else:
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    go_again = input("\nDo you want to use caesar cipher again? (y/n): ")
    if go_again == "n":
        print("Goodbye...I guess")
        break
