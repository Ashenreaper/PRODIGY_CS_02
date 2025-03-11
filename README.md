from PIL import Image

def encrypt_image(image_path, key):
    """Encrypts an image using pixel manipulation."""
    try:
        img = Image.open(image_path).convert("RGB")
        width, height = img.size
        pixels = img.load()

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Apply a simple encryption operation (e.g., XOR with the key)
                encrypted_r = (r ^ key) % 256
                encrypted_g = (g ^ key) % 256
                encrypted_b = (b ^ key) % 256
                pixels[x, y] = (encrypted_r, encrypted_g, encrypted_b)

        encrypted_image_path = image_path.rsplit('.', 1)[0] + "_encrypted.png" #save as png to preserve pixel data.
        img.save(encrypted_image_path)
        return encrypted_image_path

    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
        return None
    except Exception as e:
        print(f"An error occurred during encryption: {e}")
        return None

def decrypt_image(encrypted_image_path, key):
    """Decrypts an encrypted image."""
    try:
        img = Image.open(encrypted_image_path).convert("RGB")
        width, height = img.size
        pixels = img.load()

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Reverse the encryption operation (XOR with the key again)
                decrypted_r = (r ^ key) % 256
                decrypted_g = (g ^ key) % 256
                decrypted_b = (b ^ key) % 256
                pixels[x, y] = (decrypted_r, decrypted_g, decrypted_b)

        decrypted_image_path = encrypted_image_path.rsplit("_encrypted.png",1)[0] + "_decrypted.png"
        img.save(decrypted_image_path)
        return decrypted_image_path

    except FileNotFoundError:
        print(f"Error: Encrypted image not found at {encrypted_image_path}")
        return None
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
        return None

# Example usage
image_path = r"C:\User\VanshikaKumar\Onedrive\Pictures\your_image.jpg" # replace with your image path
encryption_key = 123  # Choose an integer key between 0 and 255

encrypted_path = encrypt_image(image_path, encryption_key)

if encrypted_path:
    print(f"Image encrypted successfully. Saved as: {encrypted_path}")
    decrypted_path = decrypt_image(encrypted_path, encryption_key)
    if decrypted_path:
        print(f"Image decrypted successfully. Saved as: {decrypted_path}")
