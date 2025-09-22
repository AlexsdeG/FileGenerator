import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import generate_random_text, create_generated_folder


def generate_svg(file_path, size_kb):
    """
    Generate an SVG file with valid structure and random data padding.
    
    Args:
        file_path (str): Path where the file will be saved
        size_kb (int): Target file size in kilobytes
    """
    # Create generated folder and get full path
    generated_folder = create_generated_folder()
    full_path = os.path.join(generated_folder, file_path)
    
    try:
        # Basic SVG header with minimal valid structure
        svg_header = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <rect width="100" height="100" fill="white"/>
'''
        
        # SVG footer
        svg_footer = '</svg>'
        
        # Calculate target size in bytes
        target_bytes = size_kb * 1024
        
        # Calculate how much random text we need
        header_size = len(svg_header.encode('utf-8'))
        footer_size = len(svg_footer.encode('utf-8'))
        remaining_bytes = target_bytes - header_size - footer_size
        
        if remaining_bytes < 0:
            print(f"Warning: Requested size ({size_kb} KB) is smaller than minimum SVG structure size.")
            # Just save the minimal SVG
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(svg_header + svg_footer)
        else:
            # Generate safe random text (only alphanumeric and basic punctuation)
            import random
            import string
            safe_chars = string.ascii_letters + string.digits + ' .,!?\n '
            
            # Calculate how much text we need (rough estimate)
            # Each character is roughly 1 byte, so we need about remaining_bytes characters
            text_length = max(remaining_bytes - 100, 100)  # Leave some margin
            comment_text = ''.join(random.choice(safe_chars) for _ in range(text_length))
            
            # Create the SVG with a comment
            svg_content = svg_header + f"  <!-- {comment_text} -->\n" + svg_footer
            
            # Write to file
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            
            # Check actual size and add more padding if needed
            actual_size = os.path.getsize(full_path)
            if actual_size < target_bytes * 0.9:  # If we're less than 90% of target
                with open(full_path, 'a', encoding='utf-8') as f:
                    extra_padding = ''.join(random.choice(safe_chars) for _ in range(target_bytes - actual_size))
                    f.write(f"  <!-- {extra_padding} -->")
        
        print(f"Successfully generated SVG file: {full_path} ({size_kb} KB)")
        
    except Exception as e:
        print(f"Error generating SVG file: {e}")
        raise