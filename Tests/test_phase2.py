#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from file_generators.image_generator import generate_png, generate_jpg
from PIL import Image

def test_phase2():
    """Test Phase 2 functionality"""
    print("Testing Phase 2: Image File Generation (Binary Formats)")
    print("=" * 60)
    
    # Test 1: Generate PNG file
    print("\n1. Testing PNG file generation...")
    png_filename = "test_image.png"
    png_size_kb = 50
    
    try:
        generate_png(png_filename, png_size_kb)
        
        # Verify file was created
        if os.path.exists(png_filename):
            file_size = os.path.getsize(png_filename)
            print(f"PNG file created: {png_filename}")
            print(f"Expected size: {png_size_kb} KB ({png_size_kb * 1024} bytes)")
            print(f"Actual size: {file_size} bytes ({file_size / 1024:.2f} KB)")
            
            # Check if size is approximately correct (allowing for small variations)
            expected_bytes = png_size_kb * 1024
            size_diff = abs(file_size - expected_bytes)
            if size_diff <= 100:  # Allow larger variations for image headers
                print("✓ PASS - File size correct")
            else:
                print(f"✗ FAIL - Size difference too large: {size_diff} bytes")
            
            # Test if it's a valid PNG by trying to open it
            try:
                img = Image.open(png_filename)
                print(f"✓ PASS - Valid PNG image format detected")
                print(f"  Image format: {img.format}")
                print(f"  Image size: {img.size}")
                img.close()
            except Exception as e:
                print(f"✗ FAIL - Invalid PNG format: {e}")
                
            # Clean up
            os.remove(png_filename)
            print("PNG test file cleaned up")
        else:
            print("✗ FAIL - PNG file was not created")
    except Exception as e:
        print(f"✗ FAIL - Exception occurred during PNG generation: {e}")
    
    # Test 2: Generate JPG file
    print("\n2. Testing JPG file generation...")
    jpg_filename = "test_image.jpg"
    jpg_size_kb = 100
    
    try:
        generate_jpg(jpg_filename, jpg_size_kb)
        
        # Verify file was created
        if os.path.exists(jpg_filename):
            file_size = os.path.getsize(jpg_filename)
            print(f"JPG file created: {jpg_filename}")
            print(f"Expected size: {jpg_size_kb} KB ({jpg_size_kb * 1024} bytes)")
            print(f"Actual size: {file_size} bytes ({file_size / 1024:.2f} KB)")
            
            # Check if size is approximately correct
            expected_bytes = jpg_size_kb * 1024
            size_diff = abs(file_size - expected_bytes)
            if size_diff <= 100:  # Allow larger variations for image headers
                print("✓ PASS - File size correct")
            else:
                print(f"✗ FAIL - Size difference too large: {size_diff} bytes")
            
            # Test if it's a valid JPG by trying to open it
            try:
                img = Image.open(jpg_filename)
                print(f"✓ PASS - Valid JPG image format detected")
                print(f"  Image format: {img.format}")
                print(f"  Image size: {img.size}")
                img.close()
            except Exception as e:
                print(f"✗ FAIL - Invalid JPG format: {e}")
                
            # Clean up
            os.remove(jpg_filename)
            print("JPG test file cleaned up")
        else:
            print("✗ FAIL - JPG file was not created")
    except Exception as e:
        print(f"✗ FAIL - Exception occurred during JPG generation: {e}")
    
    # Test 3: Small file size handling
    print("\n3. Testing small file size handling...")
    small_png = "small.png"
    small_size = 1  # 1 KB - smaller than typical PNG header
    
    try:
        generate_png(small_png, small_size)
        if os.path.exists(small_png):
            print("✓ PASS - Small PNG file created with warning")
            os.remove(small_png)
    except Exception as e:
        print(f"✗ FAIL - Small PNG generation failed: {e}")
    
    print("\nPhase 2 Testing Complete!")
    print("=" * 60)

if __name__ == "__main__":
    test_phase2()