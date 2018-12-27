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
        self.main()

    def set_key(self):
        while not self.key:
            key = input('Insert your key (sequence of alphabetic characters): ')
            if key and all([char.upper() in self.character_set for char in key]):
                self.key = key.upper()

    def process_message(self, key, decrypt=False):
        msg_code = ''
        for index_msg in range(len(self.input_message)):
            if self.input_message[index_msg] in self.punctuation_signs:
                msg_code += self.input_message[index_msg]
                continue
            tmp_key = self.letter_to_code[key[index_msg % len(key)]] + 1
            msg_code += self.encrypt_letter(self.input_message[index_msg], tmp_key) if not decrypt else self.decrypt_letter(self.input_message[index_msg], tmp_key)
        return msg_code


if __name__ == '__main__':
    vigenere_crypt = VigenereCipher()
    vigenere_crypt.run()
