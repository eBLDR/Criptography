import string


class Cipher:
    def __init__(self):
        self.mode = None
        self.input_message = ''
        self.output_message = ''
        self.needs_key = False
        self.key = None
        self.character_set = string.ascii_uppercase
        self.number_of_characters = len(self.character_set)
        self.letter_to_code = {letter: code for letter, code in zip(self.character_set, range(self.number_of_characters))}
        self.code_to_letter = {code: letter for code, letter in zip(range(self.number_of_characters), self.character_set)}
        self.possible_modes = {}

    def initialise(self):
        self.set_mode()
        self.set_message()
        if self.needs_key:
            self.set_key()
        self.display_info()

    def set_mode(self):
        for k, m in self.possible_modes.items():
            print('<{}> for {}'.format(k, m))
        while True:
            mode = input('Mode: ').upper()
            if mode in self.possible_modes.keys():
                self.mode = self.possible_modes[mode]
                break

    def set_message(self):
        while True:
            msg = input('Type your message: ')
            if msg and all([char.upper() in self.character_set if char != ' ' else True for char in msg]):
                self.input_message = msg.upper()
                break
            else:
                print('Only letters and whitespaces.')

    def set_key(self):
        raise NotImplementedError

    def display_info(self):
        print('\nMode: {}\nMessage: {}\nKey: {}'.format(self.mode, self.input_message, self.key if self.key else 'Unknown'))

    def process_message(self):
        raise NotImplementedError

    def encrypt_letter(self):
        raise NotImplementedError

    def decrypt_letter(self):
        raise NotImplementedError

    def display_output_message(self):
        if isinstance(self.output_message, str):
            print('\nProcessed message is:\n{}'.format(self.output_message))
        elif isinstance(self.output_message, dict):
            for key, msg in self.output_message.items():
                print('\nWith key {}, message is:\n{}'.format(key, msg))
