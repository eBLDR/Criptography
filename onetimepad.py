"""
One-time pad cipher (random substitution method), by BLDR 2014 (reviewed 2018)
"""
import random

from cipher import Cipher


class OneTimePadCipher(Cipher):
    def __init__(self):
        super().__init__()
        self.possible_modes.update({'E': 'Encryption', 'D': 'Decryption'})

    @staticmethod
    def cipher_info():
        print("\nThe one-time pad (OTP) is an encryption technique that cannot be cracked, but requires the use of a one-time"
              " pre-shared key the same size as, or longer than, the message being sent. In this technique, a plaintext"
              " is paired with a random secret key (also referred to as a one-time pad) an applies the substitution method.")

    def run(self):
        print('=== One-time pad cipher method ===\n')
        self.initialise()
        self.main()

    def set_key(self):
        key = ''
        if self.mode == 'Encryption':
            for letter in self.input_message:
                key += ' ' if letter == ' ' else random.choice(self.character_set)
            self.key = key
        elif self.mode == 'Decryption':
            while not self.key:
                key = input('Insert your otp key (sequence of alphabetic characters): ')
                if all([char.upper() in self.character_set if char != ' ' else True for char in key]) and len(key) >= len(self.input_message):
                    self.key = key.upper()
                else:
                    print('Wrong key - not enough valid characters provided')

    def process_message(self, key, decrypt=False):
        msg_code = ''
        for letter, char_key in zip(self.input_message, key):
            if letter == ' ':
                msg_code += ' '
                continue
            if not decrypt:
                msg_code += self.encrypt_letter(letter, self.letter_to_code[char_key])
            else:
                msg_code += self.decrypt_letter(letter, self.letter_to_code[char_key])
        return msg_code


if __name__ == '__main__':
    otp_crypt = OneTimePadCipher()
    otp_crypt.run()
