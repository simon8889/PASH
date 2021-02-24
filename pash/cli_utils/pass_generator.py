import random as rdm
import string



def split_string(string):
    return [x for x in string]
    
def some_character_in_list(list, password):
    are_in = False
    for i in password:
        if i in list:
            return True
    return are_in

CAPS = split_string(string.ascii_uppercase)
LOWS = split_string(string.ascii_lowercase)
DIGITS = split_string(string.digits)
SYMBOLS = ["#", "/", "$", "!", "-", "_", "@", "*", "+", ".", "?"]

def should_be_a_character(should_be,list, password):
    if should_be:
        return some_character_in_list(list,password)
    else:
        return not some_character_in_list(list,password)


class generator:
    def __init__(self, length = 15 ,lows = True ,caps=True, symbols = True, nums = True):
        self.length = length
        self.lows = lows
        self.caps = caps
        self.symbols = symbols
        self.nums = nums
        self.password = ""

    def __get_character_list(self):
        characters = []
        if self.lows:
            characters.append(LOWS)
        if self.caps:
            characters.append(CAPS)
        if self.symbols:
            characters.append(SYMBOLS)
        if self.nums:
            characters.append(DIGITS)
        return characters
    
    def __get_valid_dictionary(self):
        valid_dict = {"length": self.length == len(self.password)}
        valid_dict["lows"] = should_be_a_character(self.lows, LOWS, self.password)
        valid_dict["caps"] = should_be_a_character(self.caps, CAPS, self.password)
        valid_dict["symbols"] = should_be_a_character(self.symbols, SYMBOLS, self.password)
        valid_dict["nums"] = should_be_a_character(self.nums, DIGITS, self.password)
        return valid_dict
    
    def valid_password(self):
        return not False in self.__get_valid_dictionary().values() 
        
    
    def generate_pass(self):
        for _ in range(self.length):
            self.password += f"{rdm.choice(rdm.choice(self.__get_character_list()))}"
        
        if self.valid_password():
            return self.password
        else:
            self.password = ""
            return self.generate_pass()

def get_generator_by_questions(answers):
    types = list(map(lambda x: x.split(" ")[0],answers["types"]))
    length = int(answers["length"])
    caps = False
    lows = False
    nums = False
    symb = False
    if "Lowercase" in types:
        lows = True
    if "Upercase" in types:
        caps = True
    if "Numbers" in types:
        nums = True
    if "Symbols" in types:
        symb = True
    if 100 < length or length <= 0:
        length = 15
    return generator(length=length, symbols=symb, nums=nums, caps=caps, lows=lows)