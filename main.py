import string
import random

key = random.randrange(-10,10)
message = input("enter the message :")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+|}{:';><?/\[]=-,."
encrypted = ""
for i in message:
    position = alphabet.find(i)
    newposition = (position-key) % 92
    encrypted+=alphabet[newposition]
print("the encrypted message is :", encrypted)
print("key = ", key)
decrypted = ""
decrypt = input("do you want to decrypt the message y/n?")
while decrypt.lower() not in ("y", "n"):
    decrypt = input("do you want to decrypt the message y/n?")
if decrypt == "n":
    exit()
else:
    for i in encrypted:
        position2 = alphabet.find(i)
        new_position = (position2+key) % 92
        decrypted += alphabet[new_position]
print("the decrypted message is :", decrypted)
