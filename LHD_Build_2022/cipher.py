from string import ascii_letters
import string
def cipher_maker(string):
   string_list = list( ascii_letters)
   text_list = []
   for i in list(string):
      index = string_list.index(i)
      text_list.append(string_list[-index-1]+ string_list[index//4] + string_list[index//2])
   return "".join(text_list)
print("CIPHER MAKER") 
text = input("ENTER TEXT TO BE CIPHERED: ")
print(cipher_maker(text))
