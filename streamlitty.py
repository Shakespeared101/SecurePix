import random
import os
from io import BytesIO
import streamlit as st
from PIL import Image

def generate_key(size):
    key = []
    for _ in range(size):
        key.append(random.randint(0, 255))
    return key

def encrypt_image(image, key, password):
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

def main():
    st.markdown(
    """
    <style>
    body {
        background-image: url('https://media.istockphoto.com/id/174938791/photo/black-wood-background.jpg?s=612x612&w=0&k=20&c=PJ4blEgp5ihcoBVPdfzTy4tOlgguAv9cJzkvMYVD5IM=');
        background-size: cover;
    }
    </style>
    """,unsafe_allow_html=True
    )
    st.title('SecurePix - Image Encryption and Decryption')
    menu = st.radio('Menu:', ('Home', 'Encrypt Image', 'Decrypt Image'))
    
    if menu == 'Home':
        st.subheader('Welcome to SecurePix!')
        st.write("SecurePix is a cutting-edge image encryption and decryption tool, providing users with robust protection for their sensitive visuals.")
        st.write()
        st.write("Through a user-friendly interface, it facilitates secure image encryption with password-based algorithms, ensuring stringent data confidentiality.")
        st.write()
        st.write("Additionally, the tool offers seamless decryption, allowing authorized users to access protected content with ease.")
        st.write()
        st.write("With SecurePix, data integrity and privacy are paramount, ensuring peace of mind for users seeking top-tier image security")
    
    elif menu == 'Encrypt Image':
        st.subheader('Encrypt Image')
        password = st.text_input('Enter password for encryption:', type='password')
        uploaded_file = st.file_uploader('Upload an image to encrypt:')
        if st.button('Encrypt') and password and uploaded_file:
            key_size = 1024
            key = generate_key(key_size)
            encrypted_image_id = encrypt_image(uploaded_file, key, password)
            st.write(f"Image encrypted successfully. Image ID: {encrypted_image_id}")

    elif menu == 'Decrypt Image':
        st.subheader('Decrypt Image')
        image_id = st.text_input('Enter Image ID:')
        password = st.text_input('Enter password:', type='password')
        if st.button('Decrypt'):
            decrypted_image = decrypt_image(image_id, password)
            if decrypted_image:
                st.image(decrypted_image, use_column_width=True)
                with open(decrypted_image, 'rb') as f:
                    data = f.read()
                download_button = st.download_button(
                    label="Download Decrypted Image",
                    data=data,
                    file_name=f"decrypted_image_{image_id}.png",
                    mime="image/png"
                )
            else:
                st.write("Wrong image ID or password.")

if __name__ == '__main__':
    main()
