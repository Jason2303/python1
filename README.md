This Python script performs encryption and decryption using the classic Caesar Cipher technique. It shifts each letter in the plaintext by a fixed number of positions, creating a simple but effective method of securing messages that are inputed into the code.

 Features
- Encrypts any alphabetic string using a key (shift value)
- Decrypts encoded messages back to plaintext
- Handles both uppercase and lowercase letters
- Ignores non-alphabet characters (punctuation, numbers)

How to run the code:
Run the script:
python caesercipher.py

Sample usage:
encrypt("HelloWorld", 3)   # ➝ "KhoorZruog"
decrypt("KhoorZruog", 3)   # ➝ "HelloWorld"

📂 Folder Structure
caesercipher/
│
├── caesercipher.py        # Main encryption/decryption script
├── README.md              # Project overview and instructions



Technologies
- Python 3
- GitHub for version control
- Basic cryptographic concepts

