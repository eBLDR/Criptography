"""
OR, AND, XOR bitwise operators using one-time pad encryption, by BLDR 2014 (reviewed 2018)
"""
import os
import random

from PIL import Image


class BitwiseOTP:
    def __init__(self, filename):
        self.filename = filename
        self.original_array_img = []
        self.encrypted_array_img = []
        self.output_img = None
        self.possible_modes = {'OR': 'OR operand', 'AND': 'AND operand', 'XOR': 'XOR operand'}
        self.operand = ''

    @staticmethod
    def get_random_bit():
        return random.randint(1, 255)

    def run(self):
        print('=== One Time Pad using OR, AND, XOR bitwise operators ===\n')
        self.set_operand()
        self.display_info()
        self.generate_array_from_img()
        self.encrypt()
        self.generate_img_from_array()
        self.save_image()

    def display_info(self):
        print('\nOriginal image: {}\nOperand: {}'.format(self.filename, self.operand))

    def set_operand(self):
        menu_str = ''
        for k, m in self.possible_modes.items():
            menu_str += '<{}> for {}\n'.format(k, m)
        print(menu_str)
        while not self.operand:
            operand = input('Operand: ').upper()
            if operand in self.possible_modes.keys():
                self.operand = operand

    def generate_array_from_img(self):
        img = Image.open(self.filename)
        pix = img.load()
        width, height = img.size
        array = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(pix[x, y])
            array.append(row)
        self.original_array_img = array

    def encrypt(self):
        array = []
        for j in range(len(self.original_array_img)):
            row = []
            for i in self.original_array_img[j]:
                bit = self.get_random_bit()
                if self.operand == 'OR':
                    row.append(self.original_array_img[j][i] | bit)
                elif self.operand == 'AND':
                    row.append(self.original_array_img[j][i] & bit)
                elif self.operand == 'XOR':
                    row.append(self.original_array_img[j][i] ^ bit)
            array.append(row)
        self.encrypted_array_img = array

    def generate_img_from_array(self):
        width = len(self.encrypted_array_img[0])
        height = len(self.encrypted_array_img)
        img = Image.new('L', (width, height))
        for y in range(height):
            for x in range(width):
                img.putpixel((x, y), self.encrypted_array_img[y][x])
        self.output_img = img

    def save_image(self):
        filename = '{}_{}encrypted.jpg'.format(os.path.splitext(self.filename)[0], self.operand)
        self.output_img.save(filename, 'jpeg')
        print('Encrypted image saved as: {}'.format(filename))
        self.output_img.show()


if __name__ == '__main__':
    FILENAME = 'cat256x256.jpg'
    otp_img = BitwiseOTP(FILENAME)
    otp_img.run()
