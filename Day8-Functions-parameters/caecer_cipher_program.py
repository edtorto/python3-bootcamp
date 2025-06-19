

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

name = str(input("What is your name? \n")).upper()
print(f"{name}, welcome to Caeser Cipher Program!")
def ceaser(cipher_direction: str, start_text:str, shift_amount:int):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is: {end_text}")

should_continue = True
while should_continue:
    # user inputs
    direction = input("Type'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type in your message:\n").lower()
    shift = int(input("Type in the shift number: \n"))

    shift = shift % 26
    ceaser(cipher_direction=direction, start_text=text,shift_amount=shift) # call the decryption function
    
    result = str(input("Type 'yes' if you want to go again, otherwise type 'no'. \n")).lower()
    if result =="no":
        should_continue = False
        print("Goodbye")