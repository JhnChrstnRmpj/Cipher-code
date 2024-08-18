import random
import string
import os

os.system("cls")
def caesar_cipher(text, shift):
  result = ""

  for i in range(len(text)):
    
    char = text[i]

    #CHECKS IF THE TEXT IS UPPERCASE LETTER
    if char.isupper():
      result += chr((ord(char) + shift - 65) % 26 + 65) 

    #CHECKS IF THE TEXT IS A LOWERCASE LETTER
    elif char.islower():
      result += chr((ord(char) + shift - 97) % 26 + 97)

    else:
      result += char

  return result

#TEXTS NEEDED
text1 = "Geschwindigkeitsbegrenzung"
text2 = ''.join(random.choice(string.ascii_letters) for _ in range(100))

#TEXT SHIFT
shift = 5

#ENCRYPTED TEXT
encrypted_text1 = caesar_cipher(text1, shift)
encrypted_text2 = caesar_cipher(text2, shift)

#DECRYPTED TEXT
decrypted_text1 = caesar_cipher(encrypted_text1, -shift)
decrypted_text2 = caesar_cipher(encrypted_text2, -shift)

#RESULT FOR FIRST GIVEN
print("CAESAR CIPHER")
print(f"Original:  {text1}")
print(f"Encrypted:  {encrypted_text1}")
print(f"Decrypted:  {decrypted_text1}","\n")

#RESULT FOR SECOND GIVEN
print(f"Original:  {text2}")	
print(f"Encrypted:  {encrypted_text2}")
print(f"Decrypted:  {decrypted_text2}","\n")

# Pressing "enter" to end the program
input("Press 'enter' to end the program...") 
