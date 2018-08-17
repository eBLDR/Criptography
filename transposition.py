"""
Caesar cipher (substitution method) - by BLDR 2014 (reviewed 2018)
"""
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
        if self.mode == 'Cipher Info':
            self.cipher_info()
        elif self.mode == 'Encryption':
            self.output_message = self.process_message(self.key)
        elif self.mode == 'Decryption':
            self.output_message = self.process_message(self.key, decrypt=True)
        if self.output_message:
            self.display_output_message()

    def set_key(self):
        while not self.key:
            key = input('Insert key (any integer): ')
            if key.isdigit():
                self.key = int(key)

    def process_message(self, key, decrypt=False):
        if not decrypt:
            return self.encrypt_message(key)
        else:
            return self.decrypt_message(key)

    def encrypt_message(self, key):
        msg_code = ''
        for column in range(key):
            pointer = column
            while pointer < len(self.input_message):
                msg_code += self.input_message[pointer]
                pointer += key
        return msg_code

    def decrypt_message(self, key):
        from math import ceil
        msg_code = ''
        msg_length = len(self.input_message)
        pointer_jump = ceil(msg_length / key)
        for i in range(msg_length):
            pointer = (i * pointer_jump) % msg_length
            msg_code += self.input_message[pointer]
        return msg_code


if __name__ == '__main__':
    transposition_crypt = TranspositionCipher()
    transposition_crypt.run()
