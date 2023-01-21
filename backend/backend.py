from faker import Faker
import audio2numpy as a2n
import string
import math

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
digits = list(string.digits)
special_characters = list(string.punctuation)

class User:
    username = None
    master_password = None

    def __init__(self, username, master_password):
        self.username = username
        self.master_password = master_password

    def get_username(self): return self.username
    def get_master_password(self): return self.master_password

    def update_username(self, new_username):
        self.username = new_username

    def update_master_password (self, new_master_password):
        self.master_password = new_master_password


# class Password uses the Faker library to create a password from a specified
# charset, length and a seed from the website url and randomness generated
# from mic recording
class Password:

    plaintext_password = None
    entropy_bits = None

    def __init__(self, url:str,pwlen: int, 
                include_num: bool,
                include_lowercase: bool,
                include_uppercase: bool,
                include_special_char: bool):
                

        x,sr=a2n.audio_from_file("./test.mp3")
        print(x)

        # define characters used in password
        charset = []
        if include_lowercase: charset += lowercase_letters
        if include_uppercase: charset += uppercase_letters
        if include_num: charset += digits
        if include_special_char: charset += special_characters

        f0 = Faker()
        Faker.seed(url)

        self.plaintext_password = str(f0.sentence(
                                    ext_word_list=charset, nb_words = pwlen*2).
                                    replace(' ', ''))[:-1]

        self.entropy_bits = compute_bit_entropy(pwlen, len(set(self.plaintext_password)))


    
    def get_plaintext_password(self): return self.plaintext_password
    def get_entropy(self): return self.entropy_bits


# bits of entropy in string = log2(unique characters ^ length of string)
def compute_bit_entropy(string_length: int, charset_size:int)-> float:
    return math.log(charset_size**string_length,2)

if __name__ == "__main__":
    pw = Password("url", 99, True,True,True,True)
    print(pw.get_plaintext_password())
    print(pw.get_entropy())



# from faker import Faker
# import audio2numpy as a2n
# import string

# class User:
#     username = None
#     master_password = None

#     def __init__(self, username, master_password):
#         self.username = username
#         self.master_password = master_password

#     def update_username(self, new_username):
#         self.username = new_username

#     def update_master_password (self, new_master_password):
#         self.master_password = new_master_password

# class Password:

#     lowercase_letters = list(string.ascii_lowercase)
#     uppercase_letters = list(string.ascii_uppercase)
#     digits = list(string.digits)
#     special_characters = list(string.punctuation)

#     def __init__(self, url:str,len: int, 
#                 include_num: bool,
#                 include_lowercase: bool,
#                 include_uppercase: bool,
#                 include_special_char: bool):
                

#         # x,sr=a2n.audio_from_file("test.mp3")
#         # print(x)



#         f0 = Faker()
#         Faker.seed(0)

#         print(f0.sentence(ext_word_list=charset, nb_words= 99).replace(' ',''))
#         return pw

  


#     def get_lowercase_letters(self): return self.lowercase_letters
#     def get_uppercase_letters(self): return self.uppercase_letters
#     def get_digits(self): return self.digits
#     def get_special_characters(self): return self.special_characters


# if __name__ == "__main__":

#     print(Password("url", 10, True,True,True,True))
#     print(Password("url", 5, True,False,False,False))