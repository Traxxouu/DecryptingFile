from cryptography.fernet import Fernet

# Load the encryption key
with open("path_to_key/encryption_key.key", "rb") as key_file:
    key = key_file.read()

# Initialize the cipher
cipher = Fernet(key)

# Read the encrypted file
with open("path_to_encrypted_file/perl_credit_encrypted.txt", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt the data
decrypted_data = cipher.decrypt(encrypted_data)


print("Decrypted content:")
print(decrypted_data.decode("utf-8"))
