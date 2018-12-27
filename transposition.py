"""
Caesar cipher (substitution method) - by BLDR 2018
"""
from math import ceil

from cipher import Cipher


class TranspositionCipher(Cipher):
    def __init__(self):
        super().__init__()
        self.possible_modes.update({'E': 'Encryption', 'D': 'Decryption'})

    @staticmethod
    def cipher_info():
        print("Transposition cipher is a method of encryption by which the positions "
              "held by units of plaintext (which are commonly characters or groups of "
              "characters) are shifted according to a regular system, so that the ciphertext "
              "constitutes a permutation of the plaintext.")

    def run(self):
        print('=== Transposition cipher method ===\n')
        self.initialise(accept_numbers=True)
        self.main()

    def set_key(self):
        while not self.key:
            key = input('Insert key (any integer): ')
            if key.isdigit():
                self.key = int(key)

    def process_message(self, key, decrypt=False):
        msg_code = ''
        msg_length = len(self.input_message)
        pointer_jump = ceil(msg_length / key) if decrypt else key

        for index in range(pointer_jump):
            pointer = index
            while pointer < msg_length:
                msg_code += self.input_message[pointer]
                pointer += pointer_jump
        return msg_code


if __name__ == '__main__':
    transposition_crypt = TranspositionCipher()
    transposition_crypt.run()
