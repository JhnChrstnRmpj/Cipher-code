import string
import random
import os

os.system("cls")

class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard_settings, rotor_positions=None):
        self.alphabet = string.ascii_uppercase
        self.rotors = [self.create_rotor(rotor) for rotor in rotors]
        self.reflector = self.create_rotor(reflector)
        self.plugboard = self.create_plugboard(plugboard_settings)
        self.rotor_positions = rotor_positions if rotor_positions else [0] * len(rotors)
        self.initial_positions = self.rotor_positions[:]

    def create_rotor(self, wiring):
        return [self.alphabet.index(c) for c in wiring]

    def create_plugboard(self, settings):
        wiring = list(self.alphabet)
        for a, b in settings:
            a_index, b_index = self.alphabet.index(a), self.alphabet.index(b)
            wiring[a_index], wiring[b_index] = wiring[b_index], wiring[a_index]
        return wiring

    def reset_rotors(self):
        self.rotor_positions = self.initial_positions[:]

    def step_rotors(self):
        self.rotor_positions[0] = (self.rotor_positions[0] + 1) % 26
        for i in range(1, len(self.rotors)):
            if self.rotor_positions[i - 1] == 0:
                self.rotor_positions[i] = (self.rotor_positions[i] + 1) % 26

    def encipher_letter(self, letter):
        index = self.alphabet.index(letter)

        # Pass through plugboard
        index = self.alphabet.index(self.plugboard[index])

        # Pass through rotors (right to left)
        for i, rotor in enumerate(self.rotors):
            index = (rotor[(index + self.rotor_positions[i]) % 26] - self.rotor_positions[i]) % 26

        # Pass through reflector
        index = self.reflector[index]

        # Pass back through rotors (left to right)
        for i, rotor in reversed(list(enumerate(self.rotors))):
            index = (rotor.index((index + self.rotor_positions[i]) % 26) - self.rotor_positions[i]) % 26

        # Pass through plugboard again
        index = self.alphabet.index(self.plugboard[index])

        return self.alphabet[index]

    def encipher(self, text):
        encrypted_text = ""
        for letter in text:
            if letter in self.alphabet:
                self.step_rotors()
                encrypted_text += self.encipher_letter(letter)
            else:
                encrypted_text += letter
        return encrypted_text

# Define rotors, reflector, and plugboard settings
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
plugboard_settings = [('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J'), ('K', 'L'), ('M', 'N'), ('O', 'P'), ('Q', 'R'), ('S', 'T')]

# Create an instance of the Enigma machine
enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard_settings)

# Test string
test_string = "HELLOENIGMAMACHINE"

# Encrypt the test string
encrypted = enigma.encipher(test_string)

# Reset the Enigma machine to the initial state to simulate decryption
enigma.reset_rotors()

# Decrypt the encrypted string (which is just running it through the machine again)
decrypted = enigma.encipher(encrypted)

print("ENIGMA MACHINE CIPHER \n")
print(f"Original:   {test_string}")
print(f"Encrypted:  {encrypted}")
print(f"Decrypted:  {decrypted} \n")

# Show that the flaw exists: letters cannot map to themselves
test_flaw = all(test_string[i] != encrypted[i] for i in range(len(test_string)))
print(f"Flaw (letter does not map to itself): {test_flaw} \n")

# Pressing "enter" to end the program
input("Press 'enter' to end the program...") 

