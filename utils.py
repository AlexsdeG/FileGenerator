import os
import random
import string


def prompt_for_filename_and_size():
    """
    Prompt the user for a filename and target size in kilobytes.
    
    Returns:
        tuple: (filename, size_kb) where filename is a string and size_kb is an integer
    """
    while True:
        filename = input("Enter filename (with extension): ").strip()
        if not filename:
            print("Error: Filename cannot be empty. Please try again.")
            continue
        break
    
    while True:
        size_input = input("Enter target size in kilobytes (KB): ").strip()
        try:
            size_kb = int(size_input)
            if size_kb <= 0:
                print("Error: Size must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number. Please try again.")
    
    return filename, size_kb


def generate_random_bytes(size_kb):
    """
    Generate a block of random bytes of the specified size.
    
    Args:
        size_kb (int): Size in kilobytes
        
    Returns:
        bytes: Random bytes of the specified size
    """
    # Convert KB to bytes (1 KB = 1024 bytes)
    size_bytes = size_kb * 1024
    
    # Generate random bytes
    random_data = os.urandom(size_bytes)
    
    return random_data


def generate_random_text(length):
    """
    Generate a random text string of specified length.
    
    Args:
        length (int): Length of the text to generate
        
    Returns:
        str: Random text string
    """
    # Generate random text using letters, digits, and punctuation
    chars = string.ascii_letters + string.digits + string.punctuation + ' \t\n'
    return ''.join(random.choice(chars) for _ in range(length))