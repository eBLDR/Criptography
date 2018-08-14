"""
Caesar cipher (substitution method) - by BLDR 2014 (reviewed 2018)

Caesar cipher, also known as Caesar's cipher, the shift cipher,
Caesar's code or Caesar shift, is one of the simplest and most widely
known encryption techniques. It is a type of substitution cipher in
which each letter in the plaintext is replaced by a letter some
fixed number of positions down the alphabet.
"""
from cipher import Cipher


class CaesarCipher(Cipher):
    def __init__(self):
        super().__init__()
        self.possible_modes = {'E': 'Encryption', 'D': 'Decryption', 'BF': 'BruteForce'}

    def run(self):
        print('Caesar cipher method. Created by BLDR.\n')
        self.initialise()
        if self.mode == 'Encryption':
            self.output_message = self.process_message(self.key)
        elif self.mode == 'Decryption':
            self.output_message = self.process_message(self.key, decrypt=True)
        elif self.mode == 'BruteForce':
            self.output_message = self.brute_force()
        self.display_output_message()

    def set_mode(self):
        super().set_mode()
        if self.mode != 'BruteForce':
            self.needs_key = True

    def set_key(self):
        while True:
            key = input('Insert your key [1, {}] (both included): '.format(self.number_of_characters - 1))
            if key.isdigit():
                key = int(key)
                if 1 <= key <= self.number_of_characters - 1:
                    self.key = key
                    break

    def process_message(self, key, decrypt=False):
        msg_code = ''
        for letter in self.input_message:
            if letter == ' ':
                msg_code += ' '
                continue
            if not decrypt:
                new_key = self.encrypt_letter(letter, key)
            else:
                new_key = self.decrypt_letter(letter, key)
            msg_code += self.code_to_letter[new_key]
        return msg_code

    def encrypt_letter(self, letter, key):
        new_key = self.letter_to_code[letter] + key
        if new_key > self.number_of_characters - 1:
            new_key -= self.number_of_characters
        return new_key

    def decrypt_letter(self, letter, key):
        new_key = self.letter_to_code[letter] - key
        if new_key < 0:
            new_key += self.number_of_characters
        return new_key

    def brute_force(self):
        msg_code_dict = {}
        for key in range(self.number_of_characters):
            msg_code_dict[key] = self.process_message(key, decrypt=True)
        return msg_code_dict


if __name__ == '__main__':
    caesar_crypt = CaesarCipher()
    caesar_crypt.run()
