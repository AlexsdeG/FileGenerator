#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from file_generators.document_generator import generate_pdf, generate_docx
from file_generators.vector_generator import generate_svg
from PIL import Image
import xml.etree.ElementTree as ET

def demo_phase3():
    """Demonstrate Phase 3 complex document and vector file generation"""
    print("File Generator CLI Tool - Phase 3 Demo")
    print("=" * 60)
    print("Demonstrating Complex Document and Vector File Generation...")
    print()
    
    # Generate sample SVG files
    svg_files = [
        ("sample_vector1.svg", 15),
        ("sample_vector2.svg", 30),
        ("sample_vector3.svg", 50)
    ]
    
    print("SVG Files:")
    print("-" * 20)
    for filename, size_kb in svg_files:
        print(f"Generating {filename} ({size_kb} KB)...")
        try:
            generate_svg(filename, size_kb)
            
            # Verify file was created and get info
            generated_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated")
            full_path = os.path.join(generated_folder, filename)
            
            if os.path.exists(full_path):
                file_size = os.path.getsize(full_path)
                print(f"✓ Created: {filename} ({file_size} bytes)")
                
                # Try to validate SVG
                try:
                    tree = ET.parse(full_path)
                    root = tree.getroot()
                    if root.tag.endswith('svg'):
                        print(f"  Valid SVG format: {root.tag}")
                    else:
                        print(f"  Warning: Unexpected root element: {root.tag}")
                except Exception as e:
                    print(f"  Warning: Could not validate SVG: {e}")
            else:
                print(f"✗ Failed to create: {filename}")
        except Exception as e:
            print(f"✗ Error generating {filename}: {e}")
        
        print()
    
    # Generate sample PDF files
    pdf_files = [
        ("sample_doc1.pdf", 50),
        ("sample_doc2.pdf", 100),
        ("sample_doc3.pdf", 200)
    ]
    
    print("PDF Files:")
    print("-" * 20)
    for filename, size_kb in pdf_files:
        print(f"Generating {filename} ({size_kb} KB)...")
        try:
            generate_pdf(filename, size_kb)
            
            # Verify file was created and get info
            full_path = os.path.join(generated_folder, filename)
            
            if os.path.exists(full_path):
                file_size = os.path.getsize(full_path)
                print(f"✓ Created: {filename} ({file_size} bytes)")
                
                # Try to validate PDF
                try:
                    with open(full_path, 'rb') as f:
                        header = f.read(8)
                        if header.startswith(b'%PDF-1.'):
                            print(f"  Valid PDF format detected")
                        else:
                            print(f"  Warning: Invalid PDF signature")
                except Exception as e:
                    print(f"  Warning: Could not validate PDF: {e}")
            else:
                print(f"✗ Failed to create: {filename}")
        except Exception as e:
            print(f"✗ Error generating {filename}: {e}")
        
        print()
    
    # Generate sample DOCX files
    docx_files = [
        ("sample_doc1.docx", 75),
        ("sample_doc2.docx", 125),
        ("sample_doc3.docx", 200)
    ]
    
    print("DOCX Files:")
    print("-" * 20)
    for filename, size_kb in docx_files:
        print(f"Generating {filename} ({size_kb} KB)...")
        try:
            generate_docx(filename, size_kb)
            
            # Verify file was created and get info
            full_path = os.path.join(generated_folder, filename)
            
            if os.path.exists(full_path):
                file_size = os.path.getsize(full_path)
                print(f"✓ Created: {filename} ({file_size} bytes)")
                
                # Try to validate DOCX
                try:
                    with open(full_path, 'rb') as f:
                        header = f.read(4)
                        if header == b'PK\x03\x04':
                            print(f"  Valid DOCX (ZIP) format detected")
                        else:
                            print(f"  Warning: Invalid DOCX signature: {header}")
                except Exception as e:
                    print(f"  Warning: Could not validate DOCX: {e}")
            else:
                print(f"✗ Failed to create: {filename}")
        except Exception as e:
            print(f"✗ Error generating {filename}: {e}")
        
        print()
    
    print("Phase 3 Demo Complete!")
    print("\nGenerated files:")
    all_files = svg_files + pdf_files + docx_files
    for filename, _ in all_files:
        full_path = os.path.join(generated_folder, filename)
        if os.path.exists(full_path):
            size = os.path.getsize(full_path)
            print(f"  - {filename} ({size} bytes)")
    
    print("\nTo use the interactive CLI, run: python cli.py")
    print("To test functionality, run: python test_phase3.py")

if __name__ == "__main__":
    demo_phase3()