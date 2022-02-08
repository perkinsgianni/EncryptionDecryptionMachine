"""
Gianni Perkins
perkinsgianni@gmail.com
Date of completion: 10/15/21
"""
import glob
cipher_file = glob.glob("encryption_machine_fellow/cipher.txt")
cipher_str = open("cipher.txt", "r").read().strip('[]')
split_cipher_str = list(cipher_str.split(', '))
encrypted_cipher = list(map(int, split_cipher_str))
print(encrypted_cipher)

import glob
private_key_file = glob.glob("encryption_machine_fellow/private_key.txt")
private_key = open("private_key.txt", "r").read()
d = int(private_key)
print(d)

import glob
n_file = glob.glob("encryption_machine_fellow/n.txt")
n = open("n.txt", "r").read()
n = int(n)
print(n)

# Private key decryption

replacement_dictionary = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, 
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, 
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, 
        "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, 
        "Y": 25, "Z": 26, " ": 27
    }

reverse_replacement_dictionary = {value:key for key,value in replacement_dictionary.items()}
print(reverse_replacement_dictionary)

def decrypt():

    cipher_decryption = []
    for c in encrypted_cipher:
        decrypted_cipher = c ** d % n
        cipher_decryption.append(decrypted_cipher)
    print(cipher_decryption)

    global decrypted_message_list
    decrypted_message_list = []
    for num in cipher_decryption:
        decrypted_message_list.append(reverse_replacement_dictionary[num])
    print(decrypted_message_list)

decrypt()

decrypted_message = "".join(decrypted_message_list)
print(decrypted_message)

# Save decrypted message

decrypted_message_file = open("decrypted_message.txt", "w")
decrypted_message_file.write(str(decrypted_message).lower().replace('parrotit', 'parrot\nit').replace('gossipand', 'gossip\nand'))
decrypted_message_file.close()