### **Phase 1: Project Scaffolding and Core CLI Functionality**

This phase lays the foundation of the project. The goal is to create a working command-line interface, establish the project structure, and implement the simplest file generation case (a plain text file) to ensure the end-to-end workflow is operational.

*   **Substep 1.1: Initialize Project Structure**
    *   Create the root directory: `file-generator/`
    *   Create necessary subdirectories: `file-generator/file_generators/`
    *   Create Python package markers: `file-generator/file_generators/__init__.py`
    *   Create the main script: `file-generator/cli.py`
    *   Create a utility script: `file-generator/utils.py`

*   **Substep 1.2: Setup Dependencies and Documentation**
    *   Create a `requirements.txt` file and add the single dependency: `console-menu`.
    *   Create a `README.md` file with a basic project title and a brief description.

*   **Substep 1.3: Build the CLI Skeleton**
    *   In `cli.py`, import `ConsoleMenu` and `FunctionItem`.
    *   Create a main menu with placeholder sub-menus for "Image Files", "Document Files", and "Vector Files".
    *   The menu should be runnable but the items won't have functionality yet.

*   **Substep 1.4: Implement Core Utilities**
    *   In `utils.py`, create a helper function `prompt_for_filename_and_size()` that asks the user for a filename and a target size in kilobytes (KB). This function should include basic input validation to ensure the size is a positive number.
    *   In `utils.py`, create a function `generate_random_bytes(size_kb)` that returns a block of random bytes of the specified size.

*   **Substep 1.5: Implement Plain Text (TXT) File Generation**
    *   In `file_generators/document_generator.py`, create a function `generate_txt(file_path, size_kb)`.
    *   This function will use the `generate_random_bytes` utility and write the data to the specified `file_path`.
    *   In `cli.py`, create a wrapper function that calls `prompt_for_filename_and_size()` and then passes the result to `generate_txt`.
    *   Hook this wrapper function into a `FunctionItem` under the "Document Files" sub-menu.

*   **Phase 1 Testing:**
    1.  **Run the CLI:** Execute `python cli.py`. The main menu and sub-menus should appear without errors.
    2.  **Test TXT Generation:**
        *   Navigate to the "Document Files" -> "Generate TXT File" menu item.
        *   When prompted, enter a filename (e.g., `test.txt`) and a size (e.g., `10`).
        *   **Verification:** Check that a `test.txt` file is created in the root directory and that its size is approximately 10 KB.
    3.  **Test Input Validation:** Attempt to enter a non-numeric or negative value for the size. The tool should handle this gracefully with an error message and re-prompt the user.

---

### **Phase 2: Image File Generation (Binary Formats)**

This phase focuses on handling binary files with specific header requirements. It introduces the `Pillow` library to generate valid image headers, which will then be padded with random data to meet the size requirement.

*   **Substep 2.1: Add Dependencies**
    *   Add `Pillow` to the `requirements.txt` file.

*   **Substep 2.2: Create Image Generator Module**
    *   Create `file_generators/image_generator.py`.
    *   Import necessary modules from `PIL` (`Image`) and `io` (`BytesIO`).

*   **Substep 2.3: Implement PNG Generation**
    *   In `image_generator.py`, create a function `generate_png(file_path, size_kb)`.
    *   Inside, create a minimal 1x1 pixel black image using `Image.new('RGB', (1, 1))`.
    *   Save this minimal image to an in-memory `BytesIO` buffer to get its byte representation.
    *   Calculate the remaining bytes needed to reach the target size.
    *   Use the `generate_random_bytes` utility from `utils.py` to create the padding.
    *   Append the padding to the initial image bytes and write the final result to the specified `file_path`.

*   **Substep 2.4: Implement JPG/JPEG Generation**
    *   In `image_generator.py`, create a similar function `generate_jpg(file_path, size_kb)`.
    *   The process is identical to the PNG generation, but the format specified when saving to the `BytesIO` buffer will be `'JPEG'`.

*   **Substep 2.5: Integrate into CLI**
    *   In `cli.py`, add `FunctionItem`s for "Generate PNG File" and "Generate JPG File" to the "Image Files" sub-menu.
    *   Connect these items to new wrapper functions that call `generate_png` and `generate_jpg` respectively.

*   **Phase 2 Testing:**
    1.  **Generate PNG:** Create a PNG file of 50 KB.
        *   **Verification:** Check that the file size is correct. Attempt to open the file in a standard image viewer (e.g., Windows Photos, macOS Preview). The file must open without an "invalid format" error, even if it displays as a corrupted or blank image.
    2.  **Generate JPG:** Repeat the test for a JPG file of 100 KB.
        *   **Verification:** Confirm the file size is correct and that it can be opened by an image viewer, proving its header is valid.

---

### **Phase 3: Complex Document and Vector File Generation**

This phase adds support for structured, text-based formats (SVG) and complex binary formats (PDF, DOCX) using specialized libraries. The method here focuses on adding random content *within* the file's structure rather than just appending bytes.

*   **Substep 3.1: Add Dependencies**
    *   Add `fpdf2` and `python-docx` to `requirements.txt`.

*   **Substep 3.2: Implement SVG (Vector) Generation**
    *   Create `file_generators/vector_generator.py`.
    *   Implement a function `generate_svg(file_path, size_kb)`.
    *   Method: Write a basic SVG header (`<svg>...</svg>`). To pad the file, insert a large XML comment (`<!-- ... -->`) containing a random string until the desired file size is reached. This is a safe way to add arbitrary data without breaking the XML structure.

*   **Substep 3.3: Implement PDF Generation**
    *   In `file_generators/document_generator.py`, create `generate_pdf(file_path, size_kb)`.
    *   Use the `fpdf2` library to create a PDF object, add a page, and set a font.
    *   Generate a large block of random text (not bytes) and add it to the page. Because of PDF compression, you may need a loop that adds text and checks the output size until the target is met.

*   **Substep 3.4: Implement DOCX Generation**
    *   In `file_generators/document_generator.py`, create `generate_docx(file_path, size_kb)`.
    *   Use `python-docx` to create a new `Document`.
    *   Add a paragraph and fill it with a large amount of random text. Similar to PDF, this may require a loop that saves to a `BytesIO` buffer to check the size before writing the final file.

*   **Substep 3.5: Integrate into CLI**
    *   Add a "Generate SVG File" item to the "Vector Files" sub-menu.
    *   Add "Generate PDF File" and "Generate DOCX File" items to the "Document Files" sub-menu.
    *   Hook these items up to their respective generator functions in `cli.py`.

*   **Phase 3 Testing:**
    1.  **Generate SVG:** Create a 20 KB SVG file.
        *   **Verification:** Check the file size. Open the file in a modern web browser (like Chrome or Firefox). It should render as a blank page without any errors.
    2.  **Generate PDF:** Create a 200 KB PDF file.
        *   **Verification:** Check the size. Open it in a PDF reader (like Adobe Reader). It should open successfully and display one or more pages filled with random text.
    3.  **Generate DOCX:** Create a 150 KB DOCX file.
        *   **Verification:** Check the size. Open it in Microsoft Word, Google Docs, or LibreOffice. The document should open correctly and show the random text content.

---

### **Phase 4: Advanced Features and Finalization**

This final phase adds an "at your own risk" feature for power users and focuses on improving the tool's usability and documentation for release.

*   **Substep 4.1: Implement Pure Random Data Generator**
    *   Add a new sub-menu to the CLI titled "Advanced (Unsafe) Generation".
    *   In `cli.py`, create a function that takes a filename (including extension) and size from the user.
    *   This function will simply call `generate_random_bytes` and write the output to the specified filename.
    *   Add a clear warning in the menu's prologue string that these files have no valid header and are likely to be corrupt.

*   **Substep 4.2: Improve User Input**
    *   Refactor the `prompt_for_filename_and_size` utility to accept more flexible size inputs, such as "5 MB" or "1.2 GB". The function should parse this string and convert it to kilobytes internally.

*   **Substep 4.3: Finalize Documentation**
    *   Thoroughly update the `README.md` file.
    *   Include sections for:
        *   **Installation:** How to set up a virtual environment and run `pip install -r requirements.txt`.
        *   **Usage:** Instructions on how to run the tool and navigate the menus.
        *   **Features:** A list of all supported file types.
        *   **Disclaimer:** A note about the "Advanced" feature.

*   **Phase 4 Testing:**
    1.  **Test Advanced Generator:**
        *   Use the feature to create a file named `test.zip` of size `2 MB`.
        *   **Verification:** Confirm the file size is correct. Attempting to open it with an archive tool should result in a "corrupt archive" or "invalid format" error, which is the expected outcome.
    2.  **Test Enhanced Size Input:**
        *   Generate any file type using inputs like "1.5MB", "500kb", etc.
        *   **Verification:** Check that the created files have the correct corresponding sizes (e.g., ~1536 KB for 1.5 MB).
    3.  **Regression Test:** Briefly re-test one file type from each previous phase to ensure that no functionality was broken during the refactoring.