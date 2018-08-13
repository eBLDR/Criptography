"""
Caesar cipher (substitution method) - by BLDR 2014 (reviewed 2018)
"""
import string


class CaesarCipher:
    def __init__(self):
        self.mode = None
        self.possible_modes = {'E': 'Encryption', 'D': 'Decryption', 'BF': 'BruteForce'}
        self.input_message = ''
        self.output_message = ''
        self.needs_key = False
        self.key = None
        self.character_set = string.ascii_uppercase
        self.number_of_characters = len(self.character_set)
        self.letter_to_code = {letter: code for letter, code in zip(self.character_set, range(self.number_of_characters))}
        self.code_to_letter = {code: letter for code, letter in zip(range(self.number_of_characters), self.character_set)}

    def __str__(self):
        return 'Caesar cipher method. Created by BLDR.\n'

    def run(self):
        print(self.__str__())
        self.set_mode()
        self.set_message()
        if self.needs_key:
            self.set_key()

        self.display_info()

        if self.mode == 'Encryption':
            self.output_message = self.process_message(self.key)
        elif self.mode == 'Decryption':
            self.output_message = self.process_message(self.key, decrypt=True)
        elif self.mode == 'BruteForce':
            self.output_message = self.brute_force()

        self.display_output_message()

    def set_mode(self):
        for k, m in self.possible_modes.items():
            print('<{}> for {}'.format(k, m))
        while True:
            mode = input("Mode: ").upper()
            if mode in self.possible_modes.keys():
                self.mode = self.possible_modes[mode]
                if self.mode != 'BruteForce':
                    self.needs_key = True
                break

    def set_message(self):
        while True:
            msg = input("Type your message: ")
            if msg:
                self.input_message = msg.upper()
                break

    def set_key(self):
        while True:
            key = input('Insert your key [1, {}] (both included): '.format(self.number_of_characters - 1))
            if key.isdigit():
                key = int(key)
                if 1 <= key <= self.number_of_characters - 1:
                    self.key = key
                    break

    def display_info(self):
        print('\nMode: {}\nMessage: {}\nKey: {}'.format(self.mode, self.input_message, self.key if self.key else 'Unknown'))

    def process_message(self, key, decrypt=False):
        msg_code = ''
        for letter in self.input_message:
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

    def display_output_message(self):
        if isinstance(self.output_message, str):
            print('\nProcessed message is:\n{}'.format(self.output_message))
        elif isinstance(self.output_message, dict):
            for key, msg in self.output_message.items():
                print('\nWith key {}, message is:\n{}'.format(key, msg))


if __name__ == '__main__':
    caesar_crypt = CaesarCipher()
    caesar_crypt.run()
