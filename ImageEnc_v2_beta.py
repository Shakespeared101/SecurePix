import random
import os
from io import BytesIO
from flask import Flask, render_template, request, send_file
from PIL import Image

app = Flask(__name__)

def generate_key(size):
    key = []
    for _ in range(size):
        key.append(random.randint(0, 255))
    return key

def encrypt_image(image, key):
    image_data = image.read()
    image = Image.open(BytesIO(image_data))
    image_data = image.tobytes()
    encrypted_data = bytearray()
    for i in range(len(image_data)):
        encrypted_data.append(image_data[i] ^ key[i % len(key)])
    encrypted_image = Image.frombytes(image.mode, image.size, bytes(encrypted_data))
    encrypted_image_id = generate_image_id()
    encrypted_image_path = f'EncGallery/encrypted_image_{encrypted_image_id}.png'
    encrypted_image.save(encrypted_image_path)
    password = request.form['password']
    save_key_info(encrypted_image_id, password, key)
    return encrypted_image_id

def save_key_info(image_id, password, key):
    with open(f'KeyFold/key_{image_id}.txt', 'w') as key_file:
        key_file.write(f'{password}\n')
        for k in key:
            key_file.write(f'{k}\n')

def generate_image_id():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=8))

def decrypt_image(image_id, password):
    key_file_path = f'KeyFold/key_{image_id}.txt'
    if os.path.exists(key_file_path):
        with open(key_file_path, 'r') as key_file:
            file_password = key_file.readline().strip()
            if password != file_password:
                return None
            key = []
            for i in range(1024):
                key.append(int(key_file.readline().strip()))
            encrypted_image_path = f'EncGallery/encrypted_image_{image_id}.png'
            with open(encrypted_image_path, 'rb') as encrypted_file:
                encrypted_image = Image.open(encrypted_file)
                encrypted_data = encrypted_image.tobytes()
                decrypted_data = bytearray()
                for i in range(len(encrypted_data)):
                    decrypted_data.append(encrypted_data[i] ^ key[i % len(key)])
                decrypted_image = Image.frombytes(encrypted_image.mode, encrypted_image.size, bytes(decrypted_data))
                decrypted_image_path = f'DecGallery/decrypted_image_{image_id}.png'
                decrypted_image.save(decrypted_image_path)
            return decrypted_image_path
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt_page')
def encrypt_page():
    return render_template('encrypt.html')

@app.route('/decrypt_page')
def decrypt_page():
    return render_template('decrypt.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    password = request.form['password']
    key_size = 1024
    key = generate_key(key_size)
    image_id = encrypt_image(request.files['image'], key)
    return f"Image encrypted successfully. Image ID: {image_id}"

@app.route('/decrypt', methods=['POST'])
def decrypt():
    image_id = request.form['image_id']
    password = request.form['password']
    decrypted_image = decrypt_image(image_id, password)
    if decrypted_image:
        return send_file(decrypted_image, as_attachment=True)
    else:
        return "Wrong image ID or password."

if __name__ == '__main__':
    app.run(debug=True)
