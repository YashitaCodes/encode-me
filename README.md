# Text Encoding Application

This is a Python-based desktop application that allows users to input text and encode it using various algorithms, such as Base64, MD5, SHA-256, and AES. The application features a graphical user interface (GUI) built using Tkinter.

## Features

- **User-Friendly GUI**: Enter text and select encoding algorithms easily.
- **Multiple Algorithms**: Supports Base64 encoding, MD5 and SHA-256 hashing, and AES encryption.
- **Copy to Clipboard**: Encoded or hashed results can be copied directly to the clipboard.
- **Error Handling**: Includes basic error handling for invalid input.

## Project Structure

```
encoding_app/
│
├── main.py          # Main entry point for the application
├── gui.py           # GUI-related code using Tkinter
├── encoders.py      # Functions for different encoding/decoding algorithms
├── helpers.py       # Utility functions (optional)
├── requirements.txt # Required Python libraries
```

## Installation

### Prerequisites

- Python 3.6+
- Virtual environment (recommended)

### Steps

1. **Clone the repository** :

   ```bash
   git clone <repository-url>
   cd encoding_app
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python main.py
   ```

## Usage

1. Launch the application by running `main.py`.
2. Enter the text you want to encode.
3. Select the encoding algorithm (Base64, MD5, SHA-256, AES).
4. Click "Encode" to get the result.
5. You can copy the encoded result to your clipboard using the "Copy to Clipboard" button.

## Dependencies

- `tkinter`: For building the GUI.
- `cryptography`: For AES encryption.
- `pyperclip`: For copying results to the clipboard.

All dependencies are listed in `requirements.txt`.

## Future Enhancements

- Add support for more encoding algorithms.
- Include options for file encoding.
- Save encoded results to a file.

## License

This project is open-source and available under the MIT License.
