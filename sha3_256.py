from Crypto.Hash import SHA3_256

#def make_hash_object():
 #   """Makes a hash object and returns it
  #  
   # Returns:
    #    hash_object {SHA3_256} -- the hash object
    #"""
    #hash_object = SHA3_256.new()
    #return hash_object

def hash_message(plaintext):
    """Hashes a message using SHA3-256
    
    Arguments:
        plaintext {string} -- plaintext message to be hashed
    
    Returns:
        hash_digest {bytes} -- the hash in byte form
    """
    byte_message = plaintext.encode()
    hash_object = SHA3_256.new()
    hash_object.update(byte_message)
    hash_digest = hash_object.digest()
    return hash_digest