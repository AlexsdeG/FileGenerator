import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PIL import Image
from io import BytesIO
from utils import generate_random_bytes, create_generated_folder


def generate_png(file_path, size_kb):
    """
    Generate a PNG file with valid header and random data padding.
    
    Args:
        file_path (str): Path where the file will be saved
        size_kb (int): Target file size in kilobytes
    """
    # Create generated folder and get full path
    generated_folder = create_generated_folder()
    full_path = os.path.join(generated_folder, file_path)
    
    try:
        # Create a minimal 1x1 pixel black image
        img = Image.new('RGB', (1, 1), color='black')
        
        # Save the minimal image to a BytesIO buffer to get its header
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        
        # Get the header bytes
        header_bytes = buffer.getvalue()
        header_size = len(header_bytes)
        
        # Calculate remaining bytes needed
        target_bytes = size_kb * 1024
        remaining_bytes = target_bytes - header_size
        
        if remaining_bytes < 0:
            print(f"Warning: Requested size ({size_kb} KB) is smaller than minimum PNG header size.")
            # Just save the minimal image
            with open(full_path, 'wb') as f:
                f.write(header_bytes)
        else:
            # Generate random padding data (convert remaining bytes to KB for the function)
            padding_data = generate_random_bytes(remaining_bytes // 1024)
            
            # We need to make sure we get exactly the right amount of bytes
            # generate_random_bytes returns size_kb * 1024 bytes, so we need to trim or pad
            actual_padding_size = len(padding_data)
            if actual_padding_size < remaining_bytes:
                # Add more random bytes if needed
                extra_bytes = os.urandom(remaining_bytes - actual_padding_size)
                padding_data += extra_bytes
            elif actual_padding_size > remaining_bytes:
                # Trim excess bytes
                padding_data = padding_data[:remaining_bytes]
            
            # Combine header and padding
            final_data = header_bytes + padding_data
            
            # Write to file
            with open(full_path, 'wb') as f:
                f.write(final_data)
        
        print(f"Successfully generated PNG file: {full_path} ({size_kb} KB)")
        
    except Exception as e:
        print(f"Error generating PNG file: {e}")
        raise


def generate_jpg(file_path, size_kb):
    """
    Generate a JPG/JPEG file with valid header and random data padding.
    
    Args:
        file_path (str): Path where the file will be saved
        size_kb (int): Target file size in kilobytes
    """
    # Create generated folder and get full path
    generated_folder = create_generated_folder()
    full_path = os.path.join(generated_folder, file_path)
    
    try:
        # Create a minimal 1x1 pixel black image
        img = Image.new('RGB', (1, 1), color='black')
        
        # Save the minimal image to a BytesIO buffer to get its header
        buffer = BytesIO()
        img.save(buffer, format='JPEG')
        
        # Get the header bytes
        header_bytes = buffer.getvalue()
        header_size = len(header_bytes)
        
        # Calculate remaining bytes needed
        target_bytes = size_kb * 1024
        remaining_bytes = target_bytes - header_size
        
        if remaining_bytes < 0:
            print(f"Warning: Requested size ({size_kb} KB) is smaller than minimum JPEG header size.")
            # Just save the minimal image
            with open(full_path, 'wb') as f:
                f.write(header_bytes)
        else:
            # Generate random padding data (convert remaining bytes to KB for the function)
            padding_data = generate_random_bytes(remaining_bytes // 1024)
            
            # We need to make sure we get exactly the right amount of bytes
            # generate_random_bytes returns size_kb * 1024 bytes, so we need to trim or pad
            actual_padding_size = len(padding_data)
            if actual_padding_size < remaining_bytes:
                # Add more random bytes if needed
                extra_bytes = os.urandom(remaining_bytes - actual_padding_size)
                padding_data += extra_bytes
            elif actual_padding_size > remaining_bytes:
                # Trim excess bytes
                padding_data = padding_data[:remaining_bytes]
            
            # Combine header and padding
            final_data = header_bytes + padding_data
            
            # Write to file
            with open(full_path, 'wb') as f:
                f.write(final_data)
        
        print(f"Successfully generated JPG file: {full_path} ({size_kb} KB)")
        
    except Exception as e:
        print(f"Error generating JPG file: {e}")
        raise