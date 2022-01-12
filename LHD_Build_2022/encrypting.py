from cryptography import fernet
from cryptography.fernet import Fernet

message = input("Enter text to be encrpyted: ")

key = Fernet.generate_key()

fernet = Fernet(key)
 
enrpt_message = fernet.encrypt(message.encode())
print(enrpt_message)

decrpt_message = fernet.decrypt(enrpt_message).decode()
print(decrpt_message)
