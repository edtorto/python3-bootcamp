

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# user inputs
direction = input("Type'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type in your message:\n").lower()
shift = int(input("Type in the shift number: \n"))

# Encryption function
def encrypt(plain_text:str, shift_amount:int):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}")

# decryption function
def decrypt(cipher_text:str, shift_amount:int):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is: {plain_text}")
    
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift) # call the encryption function
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift) # call the decryption function
else:
    print("Wrong choice! Try again.")