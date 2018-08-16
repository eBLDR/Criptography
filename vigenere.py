"""
Vigenere, PolyAlphabetic cipher (substitution method) - by BLDR 2014 (reviewed 2018)
"""
from cipher import Cipher


class VigenereCipher(Cipher):
    def __init__(self):
        super().__init__()
        self.possible_modes.update({'E': 'Encryption', 'D': 'Decryption'})

    @staticmethod
    def cipher_info():
        print("\nIt is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers,"
              " based on the letters of a keyword, it is a form of polyalphabetic substitution.")

    def run(self):
        print('=== Vigenere, polyalphabetic cipher method ===\n')
        self.initialise()
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
            key = input('Insert your key (sequence of alphabetic characters): ')
            if key and all([char.upper() in self.character_set for char in key]):
                self.key = key.upper()

    def process_message(self, key, decrypt=False):
        msg_code = ''
        for index_msg in range(len(self.input_message)):
            if self.input_message[index_msg] == ' ':
                msg_code += ' '
                continue
            index_key = index_msg % len(key)
            msg_code += self.encrypt_letter(self.input_message[index_msg], index_key) if not decrypt else self.decrypt_letter(self.input_message[index_msg], index_key)
        return msg_code


if __name__ == '__main__':
    vigenere_crypt = VigenereCipher()
    vigenere_crypt.run()
