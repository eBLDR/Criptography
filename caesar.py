"""
Caesar cipher (substitution method) - by BLDR 2014 (reviewed 2018)
"""
from cipher import Cipher


class CaesarCipher(Cipher):
    def __init__(self):
        super().__init__()
        self.possible_modes.update({'E': 'Encryption', 'D': 'Decryption', 'BF': 'BruteForce'})

    @staticmethod
    def cipher_info():
        print("\nCaesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and "
              "most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is "
              "replaced by a letter some fixed number of positions down the alphabet.")

    def run(self):
        print('=== Caesar cipher method ===\n')
        self.initialise()
        if self.mode == 'Cipher Info':
            self.cipher_info()
        elif self.mode == 'Encryption':
            self.output_message = self.process_message(self.key)
        elif self.mode == 'Decryption':
            self.output_message = self.process_message(self.key, decrypt=True)
        elif self.mode == 'BruteForce':
            self.output_message = self.brute_force()
        if self.output_message:
            self.display_output_message()

    def set_mode(self):
        super().set_mode()
        if self.mode == 'BruteForce':
            self.needs_key = False

    def set_key(self):
        while not self.key:
            key = input('Insert your key [1, {}] (both included): '.format(self.number_of_characters - 1))
            if key.isdigit():
                key = int(key)
                if 1 <= key <= self.number_of_characters - 1:
                    self.key = key

    def process_message(self, key, decrypt=False):
        msg_code = ''
        for letter in self.input_message:
            msg_code += ' ' if letter == ' ' else self.encrypt_letter(letter, key) if not decrypt else self.decrypt_letter(letter, key)
        return msg_code

    def brute_force(self):
        msg_code_dict = {}
        for key in range(1, self.number_of_characters + 1):
            msg_code_dict[key] = self.process_message(key, decrypt=True)
        return msg_code_dict


if __name__ == '__main__':
    caesar_crypt = CaesarCipher()
    caesar_crypt.run()
