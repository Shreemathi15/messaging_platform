# messaging_platform

**Caesar Cipher**

**Working Principle:**
• A monoalphabetic substitution cipher.
• Each letter in the plaintext is shifted by a fixed number of positions down the alphabet.
• For example, with a shift of 3:
o A → D, B → E, C → F, … X → A, Y → B, Z → C.

**Encryption Steps:**
1. 2. Remove spaces or preserve them as desired.
Convert text to lowercase or uppercase (for consistency).
3. For each character:
o If it is a letter:
§ Shift it by the given number (e.g., shift = 3).
§ Wrap around if it exceeds 'z' or 'Z'.
o If not a letter (like digits or punctuation), keep it unchanged.
4. Concatenate the shifted characters to form the ciphertext.
   
**Decryption Steps:**
1. 2. For each letter in the ciphertext:
o Apply the reverse shift (i.e., shift it in the opposite direction).
o Wrap around if necessary.
Reconstruct the original message from the decrypted characters.

**Example:**
• Plaintext: hello world
• Shift: 3
• Cipher Text: khoor zruog
• Decrypted Text: hello world


**Fernet Cipher (Symmetric Encryption)**

**Working Principle:**
• Fernet is a symmetric encryption method from Python's cryptography library.
• It ensures that data is:
o Confidential (not readable without the key)
o Authenticated (verified it hasn’t been tampered with)
• It uses a secret key to both encrypt and decrypt messages.

**Encryption Steps:**
1. 2. 3. 4. Generate or load a secure Fernet key.
Convert the plaintext string into bytes.
Encrypt the bytes using the Fernet key.
The encrypted output is Base64-encoded to produce readable ciphertext.

**Decryption Steps:**
1. 2. 3. Use the same Fernet key that was used for encryption.
Convert the encrypted string (Base64) back to bytes.
Decrypt the byte string to retrieve the original plaintext.

**Example:**
• Plaintext: secure message
• Key: (a generated secure Fernet key)
• Cipher Text: gAAAAABk... (random looking Base64 string)
• Decrypted Text: secure message
