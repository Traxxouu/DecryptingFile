from cryptography.fernet import Fernet

print("""
 ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                         
                                                                         
""")

# Step 1: Generate an encryption key
key = Fernet.generate_key()

# Save the key to a file
key_file_path = "encryption_key.key"
with open(key_file_path, "wb") as key_file:
    key_file.write(key)

print(f"Encryption key saved to {key_file_path}")

# Step 2: Initialize the cipher with the key
cipher = Fernet(key)

# Step 3: Read the file to encrypt
file_to_encrypt = "file_to_encrypt.txt"  # Replace with your file path
with open(file_to_encrypt, "rb") as file:
    data = file.read()

# Step 4: Encrypt the file content
encrypted_data = cipher.encrypt(data)

# Step 5: Save the encrypted content to a new file
encrypted_file_path = "encrypted_file.txt"
with open(encrypted_file_path, "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

print(f"Encrypted file saved to {encrypted_file_path}")
