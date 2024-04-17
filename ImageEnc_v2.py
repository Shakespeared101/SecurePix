import random
import os
from PIL import Image

def generate_key(size):
    key = []
    for _ in range(size):
        key.append(random.randint(0, 255))
    return key

def encrypt_image(image_path, key):
    with open(image_path, 'rb') as image_file:
        image = Image.open(image_file)
        image_data = image.tobytes()
        encrypted_data = bytearray()
        for i in range(len(image_data)):
            encrypted_data.append(image_data[i] ^ key[i % len(key)])
        encrypted_image = Image.frombytes(image.mode, image.size, bytes(encrypted_data))
        encrypted_image_id = generate_image_id()
        encrypted_image_path = f'encrypted_image_{encrypted_image_id}.png'
        encrypted_image.save(encrypted_image_path)
        password = input("Enter the password for the encrypted image: ")
        save_key_info(encrypted_image_id, password, key)
        return encrypted_image_id, encrypted_image_path

def save_key_info(image_id, password, key):
    with open(f'key_{image_id}.txt', 'w') as key_file:
        key_file.write(f'{password}\n')
        for k in key:
            key_file.write(f'{k}\n')

def generate_image_id():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=8))

def decrypt_image():
    image_id = input("Enter the image ID: ")
    password = input("Enter the password for the encrypted image: ")
    key_file_path = f'key_{image_id}.txt'
    if os.path.exists(key_file_path):
        with open(key_file_path, 'r') as key_file:
            file_password = key_file.readline().strip()
            if password != file_password:
                print("Wrong password. Please try again.")
                return None
            key = []
            for i in range(1024):
                key.append(int(key_file.readline().strip()))
            encrypted_image_path = f'encrypted_image_{image_id}.png'
            with open(encrypted_image_path, 'rb') as encrypted_file:
                encrypted_image = Image.open(encrypted_file)
                encrypted_data = encrypted_image.tobytes()
                decrypted_data = bytearray()
                for i in range(len(encrypted_data)):
                    decrypted_data.append(encrypted_data[i] ^ key[i % len(key)])
                decrypted_image = Image.frombytes(encrypted_image.mode, encrypted_image.size, bytes(decrypted_data))
                decrypted_image_path = f'decrypted_image_{image_id}.png'
                decrypted_image.save(decrypted_image_path)
            return decrypted_image_path
    else:
        print("Image ID not found.")
        return None

def main():
    while True:
        print("Menu:")
        print("1. Encrypt the image")
        print("2. Decrypt the image")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            image_path = input("Enter the path of the image file: ")
            key_size = 1024
            key = generate_key(key_size)
            image_id, encrypted_image_path = encrypt_image(image_path, key)
            print(f"Image encrypted successfully. Image ID: {image_id}")
        elif choice == '2':
            decrypted_image = decrypt_image()
            if decrypted_image:
                print(f"Image decrypted successfully: {decrypted_image}")
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
