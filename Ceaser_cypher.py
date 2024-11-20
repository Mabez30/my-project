from art import logo
#print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(f" Type 'encode' to encrypt, type 'decode' to decrypt: \n")
message= input("type your message: ").lower()
shift_number= int(input("Type your shift number \n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text, shift):
    cipher_text=""
    for letter in plain_text:
        if letter in alphabet:
            position= alphabet.index(letter)
            new_position= (position + shift)%26
            new_letter =alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text +=letter
    print(f"Your ciper text is {cipher_text}")


#encrypt(message, shift_number)

    
def decrypt(plain_text, shift):
    cyper_text=""
    for letter in plain_text:
        if letter in alphabet:
            postion= alphabet.index(letter)
            new_position= (postion - shift)%26
            new_letter= alphabet[new_position]
            cyper_text+= new_letter
        else:
            cyper_text +=letter
    print(f"Your ciper text is {cyper_text}")

#decrypt(message, shift_number)

if direction=="encode":
    encrypt(message, shift_number)
else:
    direction=="decode"
    decrypt(message,shift_number)