from cryptography.fernet import Fernet

key = Fernet.generate_key()

fernet = Fernet(key)

input_file = "C:/Users/Bhargav/Desktop/testFile.txt"
output_file = "encryptedFile.txt"

with open(input_file, 'rb') as file:
    plaintext = file.read()

encrypted_data = fernet.encrypt(plaintext)

with open(output_file, 'wb') as file:
    file.write(encrypted_data)

input_file = "C:/Users/Bhargav/Desktop/encryptedFile.txt"
output_file = "decryptedFile.txt"

with open(input_file, 'rb') as file:
    encrypted_data = file.read()

decrypted_data = fernet.decrypt(encrypted_data)

with open(output_file, 'wb') as file:
    file.write(decrypted_data)
