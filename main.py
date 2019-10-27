import salsa20

if __name__ == "__main__":
    message = "Arifur thanks for reviewing this"
    key = salsa20.gen_key()
    encrypted_message = salsa20.encrypt_plaintext(message, key)
    print(encrypted_message)
    decrypted_message = salsa20.decrypt_message(encrypted_message, key)
    print(decrypted_message)