#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from file_generators.document_generator import generate_txt

def demo_txt_generation():
    """Demonstrate TXT file generation"""
    print("File Generator CLI Tool - Demo")
    print("=" * 40)
    print("Demonstrating TXT file generation...")
    print()
    
    # Generate a few sample files
    demo_files = [
        ("sample1.txt", 10),
        ("sample2.txt", 25),
        ("sample3.txt", 50)
    ]
    
    for filename, size_kb in demo_files:
        print(f"Generating {filename} ({size_kb} KB)...")
        try:
            generate_txt(filename, size_kb)
            
            # Verify file was created
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                print(f"✓ Created: {filename} ({file_size} bytes)")
            else:
                print(f"✗ Failed to create: {filename}")
        except Exception as e:
            print(f"✗ Error generating {filename}: {e}")
        
        print()
    
    print("Demo complete! Generated files:")
    for filename, _ in demo_files:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"  - {filename} ({size} bytes)")
    
    print("\nTo use the interactive CLI, run: python cli.py")

if __name__ == "__main__":
    demo_txt_generation()