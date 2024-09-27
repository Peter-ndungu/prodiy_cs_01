#pip install Pillow
from PIL import Image

def encrypt_image(image_path, shift):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()  # Load the image's pixel data

    # Get image dimensions
    width, height = img.size

    # Encrypt the image by modifying pixel values
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Encrypt each pixel by adding a shift value
            encrypted_pixel = (
                (r + shift) % 256, 
                (g + shift) % 256, 
                (b + shift) % 256
            )

            # Update the pixel with the new encrypted value
            pixels[x, y] = encrypted_pixel

    # Save the encrypted image
    encrypted_path = "encrypted_image.png"
    img.save(encrypted_path)
    print(f"Image encrypted and saved as {encrypted_path}")
    return encrypted_path

def decrypt_image(encrypted_path, shift):
    # Open the encrypted image
    img = Image.open(encrypted_path)
    pixels = img.load()  # Load the image's pixel data

    # Get image dimensions
    width, height = img.size

    # Decrypt the image by reversing the encryption
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Decrypt each pixel by subtracting the shift value
            decrypted_pixel = (
                (r - shift) % 256, 
                (g - shift) % 256, 
                (b - shift) % 256
            )

            # Update the pixel with the new decrypted value
            pixels[x, y] = decrypted_pixel

    # Save the decrypted image
    decrypted_path = "decrypted_image.png"
    img.save(decrypted_path)
    print(f"Image decrypted and saved as {decrypted_path}")
    return decrypted_path

def main():
    # Prompt user for input
    image_path = input("Enter the path of the image to encrypt: ")
    shift_value = int(input("Enter shift value for encryption/decryption: "))

    # Encrypt the image
    encrypted_path = encrypt_image(image_path, shift_value)

    # Decrypt the image
    decrypt_image(encrypted_path, shift_value)

if __name__ == "__main__":
    main()
