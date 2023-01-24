import random
from customtypes import CharacterTypes, OptionType


class PasswordController():
    digits: tuple[int] = tuple(range(48, 58))
    lowercase: tuple[int] = tuple(range(97, 123))
    uppercase: tuple[int] = tuple(range(65, 91))
    symbols: tuple[int] = tuple(range(33, 48)) + tuple(range(58, 65)) + tuple(range(91, 97)) + tuple(range(123, 126))

    
    def __init__(self, length: int, options: CharacterTypes):
        self.length = length
        self.selected_options = [option for option, selected in options.items() if selected]

        
    def get_random_password(self) -> str:
        result = ''
        while len(result) < self.length:
            option = random.choice(self.selected_options)
            option_char_orders = getattr(self, option)
            option_order = random.choice(option_char_orders)
            result += chr(option_order)
            
        return result
    