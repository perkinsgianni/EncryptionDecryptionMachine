"""
Gianni Perkins
perkinsgianni@gmail.com
Date of completion: 10/13/21
"""
import glob
message_to_encrypt_file = glob.glob("encryption_machine_fellow/message_to_encrypt.txt")
message_to_encrypt = open("message_to_encrypt.txt", "r").read().replace('\n', '')
print(message_to_encrypt)

#RSA key pair

p = 15
q = 19

n = p * q
phi_n = (p - 1) * (q - 1)
e = 5
d = (2 * phi_n + 1) / e

public_key = n,e
private_key = int(d)

print(public_key, private_key)

#Public key encryption

replacement_dictionary = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, 
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, 
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, 
        "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, 
        "Y": 25, "Z": 26, " ": 27
    }

def encrypt():

    num_message = []
    for letter in message_to_encrypt:
        num_message.append(replacement_dictionary[letter.upper()])
    print(num_message)

    global cipher
    cipher = []
    for num in num_message:
        c = num ** e % n
        cipher.append(c)
    print(cipher)

encrypt()

# Save cipher

cipher_file = open("cipher.txt", "w")
cipher_file.write(str(cipher))
cipher_file.close()

# Save private key

private_key_file = open("private_key.txt", "w")
private_key_file.write(str(private_key))
private_key_file.close()

# Save n

n_file = open("n.txt", "w")
n_file.write(str(n))
n_file.close()
