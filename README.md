# PyPassKeeper

PyPassKeeper is a Python-based password manager designed to securely store and manage your passwords. It provides a user-friendly interface for storing and retrieving passwords, helping you keep your sensitive information safe.

## Features

- Securely store passwords: PassVault uses encryption techniques to ensure that your passwords are stored securely.
- User-friendly interface: The application offers an intuitive interface that makes it easy to add, search, and manage passwords.
- Strong encryption: PassVault employs robust encryption algorithms to protect your passwords from unauthorized access.
- Offline storage: All your password data is stored locally on your machine, ensuring that you have complete control over your sensitive information.

## Installation

1. Clone the repository:

```
git clone https://github.com/Congeladorportatil/PyPassKeeper.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python main.py
```

## Usage

1. Launch the PyPassKeeper application.
2. Click on the "Add" button to add a new password entry.
3. Enter the web/source, username, and password for the respective account.
4. Click "Save" to store the password securely.
5. To search for a password, click on the "Search" button and enter the web/source name.
6. The application will display the corresponding username and decrypted password, if found.

## Security Considerations

- The encryption key used by PyPassKeeper is stored locally on your machine and should be kept confidential.
- It is recommended to use a strong master password to protect access to the PassVault application.
- Regularly backup the password database file to prevent data loss.

## Contributing

Contributions are welcome! If you would like to contribute to PyPassKeeper, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure that the code passes all tests.
4. Submit a pull request outlining the changes you made.

## License

PyPassKeeper is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute this project in accordance with the terms of the license.

## Acknowledgements

PyPassKeeper makes use of the following open-source libraries:

- [cryptography](https://cryptography.io/): For encryption and decryption operations.
- [tkinter](https://docs.python.org/3/library/tkinter.html): For the graphical user interface.

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact the creator.
