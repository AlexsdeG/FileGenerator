#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from file_generators.image_generator import generate_png, generate_jpg
from PIL import Image

def demo_phase2():
    """Demonstrate Phase 2 image file generation"""
    print("File Generator CLI Tool - Phase 2 Demo")
    print("=" * 50)
    print("Demonstrating Image File Generation...")
    print()
    
    # Generate sample PNG files
    png_files = [
        ("sample_image1.png", 10),
        ("sample_image2.png", 25),
        ("sample_image3.png", 50)
    ]
    
    print("PNG Files:")
    print("-" * 20)
    for filename, size_kb in png_files:
        print(f"Generating {filename} ({size_kb} KB)...")
        try:
            generate_png(filename, size_kb)
            
            # Verify file was created and get info
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                print(f"✓ Created: {filename} ({file_size} bytes)")
                
                # Try to open and get image info
                try:
                    img = Image.open(filename)
                    print(f"  Format: {img.format}, Size: {img.size}, Mode: {img.mode}")
                    img.close()
                except Exception as e:
                    print(f"  Warning: Could not verify image format: {e}")
            else:
                print(f"✗ Failed to create: {filename}")
        except Exception as e:
            print(f"✗ Error generating {filename}: {e}")
        
        print()
    
    # Generate sample JPG files
    jpg_files = [
        ("sample_image1.jpg", 15),
        ("sample_image2.jpg", 30),
        ("sample_image3.jpg", 75)
    ]
    
    print("JPG Files:")
    print("-" * 20)
    for filename, size_kb in jpg_files:
        print(f"Generating {filename} ({size_kb} KB)...")
        try:
            generate_jpg(filename, size_kb)
            
            # Verify file was created and get info
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                print(f"✓ Created: {filename} ({file_size} bytes)")
                
                # Try to open and get image info
                try:
                    img = Image.open(filename)
                    print(f"  Format: {img.format}, Size: {img.size}, Mode: {img.mode}")
                    img.close()
                except Exception as e:
                    print(f"  Warning: Could not verify image format: {e}")
            else:
                print(f"✗ Failed to create: {filename}")
        except Exception as e:
            print(f"✗ Error generating {filename}: {e}")
        
        print()
    
    print("Phase 2 Demo Complete!")
    print("\nGenerated files:")
    all_files = png_files + jpg_files
    for filename, _ in all_files:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"  - {filename} ({size} bytes)")
    
    print("\nTo use the interactive CLI, run: python cli.py")
    print("To test functionality, run: python test_phase2.py")

if __name__ == "__main__":
    demo_phase2()