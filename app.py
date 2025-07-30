from flask import Flask, render_template
from flask_socketio import SocketIO
from datetime import datetime
from cryptography.fernet import Fernet
import os

app = Flask(__name__)
socketio = SocketIO(app)

# Caesar Cipher
def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Fernet Key Setup
if not os.path.exists("secret.key"):
    with open("secret.key", "wb") as f:
        f.write(Fernet.generate_key())

with open("secret.key", "rb") as f:
    fernet_key = f.read()

fernet = Fernet(fernet_key)

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('chat message')
def handle_chat(msg):
    user = msg['user'].strip()
    text = msg['text']
    shift = int(msg.get('shift', 3))
    cipher = msg.get('cipher', 'caesar').lower()
    timestamp = datetime.now().strftime('%I:%M %p')

    if cipher == 'caesar':
        encrypted = caesar_encrypt(text, shift)
        decrypted = caesar_decrypt(encrypted, shift)
    elif cipher == 'fernet':
        encrypted = fernet.encrypt(text.encode()).decode()
        decrypted = fernet.decrypt(encrypted.encode()).decode()
    else:
        encrypted = decrypted = text  # fallback

    socketio.emit('chat message', {
        'user': user,
        'encrypted_text': encrypted,
        'decrypted_text': decrypted,
        'cipher_type': cipher.upper(),
        'timestamp': timestamp
    })

if __name__ == '__main__':
    socketio.run(app, debug=True)
