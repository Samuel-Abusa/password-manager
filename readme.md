# Password Manager

## Overview

This Python-based Password Manager is a simple and secure application that allows users to generate, store, and retrieve passwords for various websites. The user interface is built using `Tkinter`, making it easy to use, even for beginners.

## Features

1. **Password Generation**: 
   - The application can generate strong and random passwords using letters, numbers, and symbols.
   - The generated password is automatically copied to the clipboard for easy pasting.

2. **Password Storage**: 
   - Passwords, along with the associated website and email/username, are securely stored in a JSON file (`data.json`).
   - The program checks if the fields are empty before saving the password to avoid incomplete entries.

3. **Password Retrieval**:
   - Users can search for stored passwords by entering the website name. If the website is found in the JSON file, the associated email/username and password are displayed in a pop-up window.

4. **User Interface**:
   - The user interface is built using `Tkinter`, providing an intuitive and easy-to-navigate layout.
   - The application includes buttons for generating passwords, saving passwords, and searching for saved passwords.

## How It Works

### Password Generation

The `Generator` class handles password generation. It creates a password consisting of a random mix of letters, numbers, and symbols. The length of each character type is randomly determined, ensuring variability in the generated passwords.

### Saving Passwords

Passwords, along with the corresponding website and email/username, are saved in a JSON file (`data.json`). If the file doesn't exist, the program creates it. If the file already exists, the new password is added without overwriting the existing data.

### Retrieving Passwords

When searching for a password, the program looks up the website name in the JSON file. If found, the corresponding email/username and password are displayed.

## Installation and Setup

1. **Clone the Repository**:
   - Clone this repository to your local machine.

   ```bash
   git clone https://github.com/Samuel-Abusa/password-manager.git
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   - Ensure you have Python installed on your system.
   - Install the necessary dependencies using `pip`:

   ```bash
   pip install pyperclip password-generator
   ```

3. **Run the Application**:
   - Execute the script to launch the Password Manager:

   ```bash
   python password_manager.py
   ```

## Usage

1. **Generating a Password**:
   - Enter the website name and your email/username.
   - Click on the "Generate Password" button to create a new password.
   - The generated password will appear in the password entry field and will be automatically copied to your clipboard.

2. **Saving a Password**:
   - After generating a password, click the "Add" button to save the website, email/username, and password to the JSON file.

3. **Retrieving a Password**:
   - To find a saved password, enter the website name and click the "Search" button.
   - If the website exists in the JSON file, the saved email/username and password will be displayed in a pop-up window.

## File Structure

```plaintext
├── password_manager.py  # Main application file
├── generator.py         # Password generator class
├── data.json            # JSON file storing the passwords
├── logo.png             # Logo image for the UI
└── README.md            # Readme file
```

## Dependencies

- `tkinter`: Used to build the graphical user interface.
- `json`: For storing and retrieving passwords in JSON format.
- `pyperclip`: To copy generated passwords to the clipboard.
- `password-generator`: Custom module to generate random passwords.

## Notes

- The `data.json` file is created automatically when the first password is saved. Ensure the application has permission to write files in the directory where it is executed.
- This application does not provide encryption for the stored passwords. For more secure password storage, consider encrypting the JSON file.

## License

This project is licensed under the MIT License - see the LICENSE file for details.