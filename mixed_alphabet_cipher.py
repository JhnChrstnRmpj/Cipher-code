import random
import string
import os

os.system("cls")

def generate_cipher_alphabet():
    # Get the regular alphabet
    alphabet = list(string.ascii_lowercase)
    # Shuffle the alphabet to create a cipher
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    return ''.join(alphabet), ''.join(shuffled_alphabet)

def encrypt_message(plain_text, alphabet, cipher_alphabet):
    encrypted_message = []
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            index = alphabet.index(char.lower())
            encrypted_char = cipher_alphabet[index]
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_message.append(encrypted_char)
        else:
            encrypted_message.append(char)
    return ''.join(encrypted_message)

def decrypt_message(encrypted_text, alphabet, cipher_alphabet):
    decrypted_message = []
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            index = cipher_alphabet.index(char.lower())
            decrypted_char = alphabet[index]
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_message.append(decrypted_char)
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)

# Generate the alphabets
alphabet, cipher_alphabet = generate_cipher_alphabet()

# Display the alphabets
print("MIXED ALPHABET CIPHER")
print("Regular Alphabet: ", alphabet)
print("Cipher Alphabet:  ", cipher_alphabet)

# Example usage
text1 = "Verbraucherschutzgesetz"
text2 = ''.join(random.choice(string.ascii_letters) for _ in range(100))

#ENCRYPTED TEXT
encrypted_text1 = encrypt_message(text1, alphabet, cipher_alphabet)
encrypted_text2 = encrypt_message(text2, alphabet, cipher_alphabet)

#DECRYPTED TEXT
decrypted_text1 = decrypt_message(encrypted_text1, alphabet, cipher_alphabet)
decrypted_text2 = decrypt_message(encrypted_text2, alphabet, cipher_alphabet)

#RESULT FOR FIRST GIVEN
print("\nPlain Text:      ", text1)
print("Encrypted Text:  ", encrypted_text1)
print("Decrypted Text:  ", decrypted_text1, "\n")

#RESULT FOR SECOND GIVEN
print("Plain Text:      ", text2)
print("Encrypted Text:  ", encrypted_text2)
print("Decrypted Text:  ", decrypted_text2, "\n")
