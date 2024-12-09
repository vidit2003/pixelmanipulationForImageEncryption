from PIL import Image
import numpy as np
import os

# Function to encrypt an image using XOR operation
def encrypt_image(input_image_path, key):
    # Load the image and convert it to an array
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Apply XOR operation with the key to encrypt
    encrypted_array = np.bitwise_xor(image_array, key)

    # Convert the encrypted array back to an image and save
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save('encrypted_image.png')
    print("Encryption complete. Saved as 'encrypted_image.png'.")

# Function to decrypt an image using XOR operation (same operation as encryption)
def decrypt_image(encrypted_image_path, key):
    # Load the encrypted image and convert it to an array
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_image)

    # Apply XOR operation with the key to decrypt
    decrypted_array = np.bitwise_xor(encrypted_array, key)

    # Convert the decrypted array back to an image and save
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save('decrypted_image.png')
    print("Decryption complete. Saved as 'decrypted_image.png'.")

# Generate a key for XOR operation (same size as the image)
def generate_key(image_array):
    # Generate a random key array of the same shape as the image array
    key = np.random.randint(0, 256, image_array.shape, dtype=np.uint8)
    return key

# Main function
if _name_ == "_main_":
    # Replace 'input_image.png' with the real path to your image file
    input_image_path = '/home/sam/Documents/python/5task/input_image.png'  # Full path to your image file

    # Open the image to generate the image array and the key
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Generate a key
    key = generate_key(image_array)

    # Encrypt the image
    encrypt_image(input_image_path, key)

    # Decrypt the image (use the generated key)
    decrypt_image('encrypted_image.png', key)
