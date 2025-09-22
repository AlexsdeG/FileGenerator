import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import generate_random_bytes


def generate_txt(file_path, size_kb):
    """
    Generate a plain text file with random data.
    
    Args:
        file_path (str): Path where the file will be saved
        size_kb (int): Target file size in kilobytes
    """
    # Generate random bytes
    random_data = generate_random_bytes(size_kb)
    
    # Write to file
    with open(file_path, 'wb') as f:
        f.write(random_data)
    
    print(f"Successfully generated TXT file: {file_path} ({size_kb} KB)")