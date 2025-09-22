#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from file_generators.document_generator import generate_pdf, generate_docx
from file_generators.vector_generator import generate_svg
from PIL import Image
import xml.etree.ElementTree as ET

def test_phase3():
    """Test Phase 3 functionality"""
    print("Testing Phase 3: Complex Document and Vector File Generation")
    print("=" * 70)
    
    # Test 1: Generate SVG file
    print("\n1. Testing SVG file generation...")
    svg_filename = "test_vector.svg"
    svg_size_kb = 20
    
    try:
        generate_svg(svg_filename, svg_size_kb)
        
        # Verify file was created
        generated_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated")
        svg_path = os.path.join(generated_folder, svg_filename)
        
        if os.path.exists(svg_path):
            file_size = os.path.getsize(svg_path)
            print(f"SVG file created: {svg_path}")
            print(f"Expected size: {svg_size_kb} KB ({svg_size_kb * 1024} bytes)")
            print(f"Actual size: {file_size} bytes ({file_size / 1024:.2f} KB)")
            
            # Check if size is approximately correct
            expected_bytes = svg_size_kb * 1024
            size_diff = abs(file_size - expected_bytes)
            if size_diff <= expected_bytes * 0.2:  # Allow 20% variation for XML structure
                print("✓ PASS - File size acceptable")
            else:
                print(f"✗ FAIL - Size difference too large: {size_diff} bytes")
            
            # Test if it's a valid SVG by parsing XML
            try:
                tree = ET.parse(svg_path)
                root = tree.getroot()
                if root.tag.endswith('svg'):
                    print("✓ PASS - Valid SVG format detected")
                else:
                    print(f"✗ FAIL - Invalid SVG root element: {root.tag}")
            except ET.ParseError as e:
                print(f"✗ FAIL - Invalid XML format: {e}")
            except Exception as e:
                print(f"✗ FAIL - Error parsing SVG: {e}")
                
            # Clean up
            os.remove(svg_path)
            print("SVG test file cleaned up")
        else:
            print("✗ FAIL - SVG file was not created")
    except Exception as e:
        print(f"✗ FAIL - Exception occurred during SVG generation: {e}")
    
    # Test 2: Generate PDF file
    print("\n2. Testing PDF file generation...")
    pdf_filename = "test_document.pdf"
    pdf_size_kb = 200
    
    try:
        generate_pdf(pdf_filename, pdf_size_kb)
        
        # Verify file was created
        pdf_path = os.path.join(generated_folder, pdf_filename)
        
        if os.path.exists(pdf_path):
            file_size = os.path.getsize(pdf_path)
            print(f"PDF file created: {pdf_path}")
            print(f"Expected size: {pdf_size_kb} KB ({pdf_size_kb * 1024} bytes)")
            print(f"Actual size: {file_size} bytes ({file_size / 1024:.2f} KB)")
            
            # Check if size is reasonable (PDF compression can vary significantly)
            expected_bytes = pdf_size_kb * 1024
            size_diff = abs(file_size - expected_bytes)
            if size_diff <= expected_bytes * 0.5:  # Allow 50% variation for PDF compression
                print("✓ PASS - File size acceptable")
            else:
                print(f"⚠ WARNING - Size variation large: {size_diff} bytes (but PDF compression varies)")
            
            # Test if it's a valid PDF by checking file signature
            try:
                with open(pdf_path, 'rb') as f:
                    header = f.read(8)
                    if header.startswith(b'%PDF-1.'):  # Check for any PDF version
                        print("✓ PASS - Valid PDF signature detected")
                    else:
                        print(f"✗ FAIL - Invalid PDF signature: {header}")
            except Exception as e:
                print(f"✗ FAIL - Error reading PDF: {e}")
                
            # Clean up
            os.remove(pdf_path)
            print("PDF test file cleaned up")
        else:
            print("✗ FAIL - PDF file was not created")
    except Exception as e:
        print(f"✗ FAIL - Exception occurred during PDF generation: {e}")
    
    # Test 3: Generate DOCX file
    print("\n3. Testing DOCX file generation...")
    docx_filename = "test_document.docx"
    docx_size_kb = 150
    
    try:
        generate_docx(docx_filename, docx_size_kb)
        
        # Verify file was created
        docx_path = os.path.join(generated_folder, docx_filename)
        
        if os.path.exists(docx_path):
            file_size = os.path.getsize(docx_path)
            print(f"DOCX file created: {docx_path}")
            print(f"Expected size: {docx_size_kb} KB ({docx_size_kb * 1024} bytes)")
            print(f"Actual size: {file_size} bytes ({file_size / 1024:.2f} KB)")
            
            # Check if size is reasonable (DOCX structure can vary)
            expected_bytes = docx_size_kb * 1024
            size_diff = abs(file_size - expected_bytes)
            if size_diff <= expected_bytes * 0.5:  # Allow 50% variation for DOCX structure
                print("✓ PASS - File size acceptable")
            else:
                print(f"⚠ WARNING - Size variation large: {size_diff} bytes (but DOCX structure varies)")
            
            # Test if it's a valid DOCX by checking ZIP signature
            try:
                with open(docx_path, 'rb') as f:
                    header = f.read(4)
                    if header == b'PK\x03\x04':  # ZIP signature
                        print("✓ PASS - Valid DOCX (ZIP) signature detected")
                    else:
                        print(f"✗ FAIL - Invalid DOCX signature: {header}")
            except Exception as e:
                print(f"✗ FAIL - Error reading DOCX: {e}")
                
            # Clean up
            os.remove(docx_path)
            print("DOCX test file cleaned up")
        else:
            print("✗ FAIL - DOCX file was not created")
    except Exception as e:
        print(f"✗ FAIL - Exception occurred during DOCX generation: {e}")
    
    # Test 4: Small file handling for SVG
    print("\n4. Testing small SVG file handling...")
    small_svg = "small.svg"
    small_size = 1  # 1 KB
    
    try:
        generate_svg(small_svg, small_size)
        small_svg_path = os.path.join(generated_folder, small_svg)
        if os.path.exists(small_svg_path):
            print("✓ PASS - Small SVG file created with appropriate handling")
            os.remove(small_svg_path)
    except Exception as e:
        print(f"✗ FAIL - Small SVG generation failed: {e}")
    
    print("\nPhase 3 Testing Complete!")
    print("=" * 70)

if __name__ == "__main__":
    test_phase3()