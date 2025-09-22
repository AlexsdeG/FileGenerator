#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from file_generators.document_generator import generate_txt
from utils import generate_random_bytes, generate_random_text

def test_phase1():
    """Test Phase 1 functionality"""
    print("Testing Phase 1: Project Scaffolding and Core CLI Functionality")
    print("=" * 60)
    
    # Test 1: Generate random bytes
    print("\n1. Testing generate_random_bytes function...")
    random_data = generate_random_bytes(10)  # 10 KB
    print(f"Generated {len(random_data)} bytes of random data")
    print(f"Expected: {10 * 1024} bytes")
    print(f"Actual: {len(random_data)} bytes")
    print("✓ PASS" if len(random_data) == 10 * 1024 else "✗ FAIL")
    
    # Test 2: Generate random text
    print("\n2. Testing generate_random_text function...")
    random_text = generate_random_text(100)
    print(f"Generated {len(random_text)} characters of random text")
    print(f"Expected: 100 characters")
    print(f"Actual: {len(random_text)} characters")
    print("✓ PASS" if len(random_text) == 100 else "✗ FAIL")
    
    # Test 3: Generate TXT file
    print("\n3. Testing generate_txt function...")
    test_filename = "test_output.txt"
    test_size_kb = 5
    
    try:
        generate_txt(test_filename, test_size_kb)
        
        # Verify file was created
        if os.path.exists(test_filename):
            file_size = os.path.getsize(test_filename)
            print(f"File created: {test_filename}")
            print(f"Expected size: {test_size_kb} KB ({test_size_kb * 1024} bytes)")
            print(f"Actual size: {file_size} bytes ({file_size / 1024:.2f} KB)")
            
            # Check if size is approximately correct (allowing for small variations)
            expected_bytes = test_size_kb * 1024
            size_diff = abs(file_size - expected_bytes)
            if size_diff <= 10:  # Allow small variations
                print("✓ PASS")
            else:
                print(f"✗ FAIL - Size difference too large: {size_diff} bytes")
                
            # Clean up
            os.remove(test_filename)
            print("Test file cleaned up")
        else:
            print("✗ FAIL - File was not created")
    except Exception as e:
        print(f"✗ FAIL - Exception occurred: {e}")
    
    print("\nPhase 1 Testing Complete!")
    print("=" * 60)

if __name__ == "__main__":
    test_phase1()