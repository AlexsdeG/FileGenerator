#!/usr/bin/env python3

import os
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem, SubmenuItem
from consolemenu.format import AsciiBorderStyle

from file_generators.document_generator import generate_txt
from file_generators.image_generator import generate_png, generate_jpg
from utils import prompt_for_filename_and_size


def generate_txt_wrapper():
    """Wrapper function for TXT file generation"""
    try:
        filename, size_kb = prompt_for_filename_and_size()
        generate_txt(filename, size_kb)
    except Exception as e:
        print(f"Error generating TXT file: {e}")
    
    input("\nPress Enter to continue...")


def generate_png_wrapper():
    """Wrapper function for PNG file generation"""
    try:
        filename, size_kb = prompt_for_filename_and_size()
        generate_png(filename, size_kb)
    except Exception as e:
        print(f"Error generating PNG file: {e}")
    
    input("\nPress Enter to continue...")


def generate_jpg_wrapper():
    """Wrapper function for JPG file generation"""
    try:
        filename, size_kb = prompt_for_filename_and_size()
        generate_jpg(filename, size_kb)
    except Exception as e:
        print(f"Error generating JPG file: {e}")
    
    input("\nPress Enter to continue...")


def create_image_files_menu():
    """Create the Image Files sub-menu"""
    image_menu = ConsoleMenu("Image Files", "Select an image file type to generate:")
    image_menu.border_style = AsciiBorderStyle()
    
    # Add PNG and JPG generation (Phase 2)
    image_menu.append_item(FunctionItem("Generate PNG File", generate_png_wrapper))
    image_menu.append_item(FunctionItem("Generate JPG File", generate_jpg_wrapper))
    
    return image_menu


def create_document_files_menu():
    """Create the Document Files sub-menu"""
    document_menu = ConsoleMenu("Document Files", "Select a document file type to generate:")
    document_menu.border_style = AsciiBorderStyle()
    
    # Add TXT generation (Phase 1)
    document_menu.append_item(FunctionItem("Generate TXT File", generate_txt_wrapper))
    
    # Placeholder items for Phase 3
    # document_menu.append_item(FunctionItem("Generate PDF File", generate_pdf_wrapper))
    # document_menu.append_item(FunctionItem("Generate DOCX File", generate_docx_wrapper))
    
    return document_menu


def create_vector_files_menu():
    """Create the Vector Files sub-menu"""
    vector_menu = ConsoleMenu("Vector Files", "Select a vector file type to generate:")
    vector_menu.border_style = AsciiBorderStyle()
    
    # Placeholder items for Phase 3
    # vector_menu.append_item(FunctionItem("Generate SVG File", generate_svg_wrapper))
    
    return vector_menu


def main():
    """Main application entry point"""
    # Create the main menu
    main_menu = ConsoleMenu(
        "File Generator CLI Tool",
        "Select a file category to generate:",
    )
    main_menu.border_style = AsciiBorderStyle()
    
    # Create sub-menus
    image_menu = create_image_files_menu()
    document_menu = create_document_files_menu()
    vector_menu = create_vector_files_menu()
    
    # Add sub-menu items to main menu
    main_menu.append_item(SubmenuItem("Image Files", image_menu, main_menu))
    main_menu.append_item(SubmenuItem("Document Files", document_menu, main_menu))
    main_menu.append_item(SubmenuItem("Vector Files", vector_menu, main_menu))
    
    # Show the menu
    main_menu.show()


if __name__ == "__main__":
    main()