from faker import Faker
import audio2numpy as a2n
import string

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

    def update_username(self, new_username):
        self.username = new_username

    def update_master_password (self, new_master_password):
        self.master_password = new_master_password

class Password:

    plaintext_password = ""

    def __init__(self, url:str,len: int, 
                include_num: bool,
                include_lowercase: bool,
                include_uppercase: bool,
                include_special_char: bool):
                

        # x,sr=a2n.audio_from_file("test.mp3")
        # print(x)

        charset = []
        if include_lowercase: charset += lowercase_letters
        if include_uppercase: charset += uppercase_letters
        if include_num: charset += digits
        if include_special_char: charset += special_characters

        f0 = Faker()
        Faker.seed(0)

        self.plaintext_password = str(f0.sentence(ext_word_list=charset, nb_words= len).replace(' ',''))

    
    def get_plaintext_password(self): return self.plaintext_password


if __name__ == "__main__":
    print(Password("url", 10, True,True,True,True).get_plaintext_password())
    print(Password("url", 5, True,False,False,False).get_plaintext_password())


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