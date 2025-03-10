from PIL import Image
import os

def encrypt_image(image_path, output_path, key):
    """Encrypts an image using pixel manipulation."""
    try:
        img = Image.open(image_path).convert("RGB")
        width, height = img.size
        pixels = img.load()

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (
                    (r + key) % 256,
                    (g + key) % 256,
                    (b + key) % 256,
                )

        img.save(output_path)
        print(f"Image encrypted and saved to {output_path}")

    except FileNotFoundError:
        print("Error: Image file not found.")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_image(image_path, output_path, key):
    """Decrypts an image using pixel manipulation."""
    try:
        img = Image.open(image_path).convert("RGB")
        width, height = img.size
        pixels = img.load()

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (
                    (r - key) % 256,
                    (g - key) % 256,
                    (b - key) % 256,
                )

        img.save(output_path)
        print(f"Image decrypted and saved to {output_path}")

    except FileNotFoundError:
        print("Error: Image file not found.")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

def get_valid_input(prompt, input_type, validation_func=None):
    """Gets valid user input with optional validation."""
    while True:
        try:
            user_input = input_type(input(prompt))
            if validation_func is None or validation_func(user_input):
                return user_input
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input type. Please enter a valid value.")
        except Exception as e:
          print(f"An unexpected error occured: {e}")

def file_exists(filepath):
    """Check if a file exists."""
    return os.path.exists(filepath)

if __name__ == "__main__":
    while True:
        print("\nImage Encryption/Decryption Tool")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")

        choice = get_valid_input("Enter your choice (1, 2, or 3): ", int, lambda x: 1 <= x <= 3)

        if choice == 1:
            image_file = get_valid_input("Enter the path to the image file: ", str, file_exists)
            encrypted_file = get_valid_input("Enter the path to save the encrypted image: ", str)
            encryption_key = get_valid_input("Enter the encryption key (integer): ", int)
            encrypt_image(image_file, encrypted_file, encryption_key)

        elif choice == 2:
            encrypted_file = get_valid_input("Enter the path to the encrypted image file: ", str, file_exists)
            decrypted_file = get_valid_input("Enter the path to save the decrypted image: ", str)
            decryption_key = get_valid_input("Enter the decryption key (integer): ", int)
            decrypt_image(encrypted_file, decrypted_file, decryption_key)

        elif choice == 3:
            print("Exiting...")
            break