from Crypto.Cipher import Salsa20
import os, sys

def gen_key():    
    """Generates a salsa key using 32 random bytes
    
    Returns:
        key {bytes} -- A salsa20 key
    """
    # generates random 32 bytes of data. this will serve as the key
    key = os.urandom(32)
    return key

def import_key(file_name):
    """Imports a key from a file name and returns it
    
    Arguments:
        file_name {string} -- file path
    
    Returns:
        key {bytes} -- a salsa20 key
    """
    # opens a file in read mode
    read = open(file_name, 'rb')
    # read the key into a variable named "key"
    key = read.read()
    return key

def encrypt_plaintext(plaintext, key):
    """Takes a plaintext message and encrypts it using a Salsa20 key
    
    Arguments:
        plaintext {string} -- unencrypted message
        key {bytes} -- a Salsa20 key
    
    Returns:
        encrypted_message {bytes} -- the encrypted message
    """
    # encodes the plaintext into bytes so that it can be encrypted
    byte_plaintext = plaintext.encode()
    # makes a Salsa20 cipher from the key
    cipher = Salsa20.new(key)
    # turns the plaintext message into the encrtyped version
    encrypted_message = cipher.nonce + cipher.encrypt(byte_plaintext)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """Takes an encrypted message and converts it back into plaintext using a Salsa20 key
    
    Arguments:
        encrypted_message {bytes} -- the encrypted message that needs to be converted into plaintext
        key {bytes} -- the Salsa20 key
    
    Returns:
        plaintext {string} -- the unencrypted message
    """
    # takes the nonce from the message
    msg_nonce = encrypted_message[:8]
    # takes the actual ciphertext from the message
    ciphertext = encrypted_message[8:]
    # generates a cipher from the key and the nonce
    cipher = Salsa20.new(key, nonce=msg_nonce)
    # decrypts the encrypted message back into plaintext
    byte_plaintext = cipher.decrypt(ciphertext)
    # converts the plaintext bytes into a string
    plaintext = byte_plaintext.decode()
    return plaintext


    