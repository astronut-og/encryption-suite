import salsa20
import sha3_256

if __name__ == "__main__":
    message = "testing please work"
    hash_1 = sha3_256.hash_message(message)
    hash_2 = sha3_256.hash_message(message)
    hash_3 = sha3_256.hash_message("texting please work") 