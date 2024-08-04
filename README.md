# SecurePix: Secure Image Encryption Software

## Project Overview

SecurePix is an advanced image encryption software designed to secure image data using XOR encryption. The software generates a random key for encryption and securely XORs the bytes of image pixels with this key. It supports multi-image encryption and implements efficient storage management techniques, assigning unique IDs to each image and integrating password-based authentication for secure access.

## Key Features

### XOR Encryption
- **Random Key Generation:** Generates a random key for each image to ensure unique and secure encryption.
- **XOR Operation:** Encrypts image data by XOR-ing the bytes of image pixels with the generated key, providing robust protection against unauthorized access.

### Multi-Image Encryption
- **Batch Processing:** Supports the encryption of multiple images simultaneously, enhancing efficiency and usability.
- **Unique ID Assignment:** Assigns a unique ID to each encrypted image for easy tracking and management.

### Storage Management
- **Efficient Storage:** Manages storage efficiently by segregating encrypted and decrypted image files into separate databases.
- **Password-Based Authentication:** Ensures secure access to encrypted images through password-based authentication mechanisms.

## Frontend Integration

### User-Friendly Interface with Streamlit
- **Streamlit Frontend:** Implements a user-friendly interface using Streamlit, allowing easy management of encrypted and decrypted images.
- **Passkey Management:** Facilitates easy management of passkey files for each image, ensuring secure encryption and decryption processes.

#### Features of the Streamlit Frontend
1. **Image Upload and Encryption:**
   - Users can upload multiple images for encryption.
   - The software generates and stores a unique random key for each image.
   - Images are encrypted using the XOR encryption method.

2. **Passkey Management:**
   - Provides an intuitive interface for managing passkey files associated with each encrypted image.
   - Users can download and store passkey files securely.

3. **Password-Based Access:**
   - Implements password-based authentication for accessing encrypted images.
   - Ensures that only authorized users can decrypt and view the images.

4. **Encrypted and Decrypted Image Databases:**
   - Maintains separate databases for encrypted and decrypted image files.
   - Provides easy access and management of both encrypted and decrypted images through the Streamlit interface.

5. **Decryption and Viewing:**
   - Allows users to select encrypted images and provide the corresponding passkey and password for decryption.
   - Decrypted images can be viewed and managed within the application.

## System Components

### Encryption Process
- **Key Generation:** A unique random key is generated for each image.
- **XOR Encryption:** Each pixel's byte data is XOR-ed with the generated key to produce the encrypted image.

### Storage Management
- **Image Databases:** Encrypted and decrypted images are stored in separate databases for organized and efficient management.
- **Unique IDs:** Each image is assigned a unique ID for tracking and retrieval purposes.

### Authentication
- **Password Protection:** Password-based authentication ensures that only authorized users can access encrypted images.
- **Passkey Files:** Unique passkey files are generated for each image, required for the decryption process.

## Contributors
- **Saranya Sarathy**
- **Shakthi B**

## Contact Information
For further information or support, please contact the project contributors.

---

SecurePix exemplifies the combination of robust encryption techniques and user-friendly frontend design, providing a secure and efficient solution for image data protection. With the integration of Streamlit, users can easily manage encrypted and decrypted images, ensuring a seamless and secure experience.
