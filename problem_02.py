# If you have a message you want to transmit securely, you can encrypt it (translate it into a secret code). One of the simplest ways to do this is with a shift cipher.
# Famously, Julius Caesar used this type of cipher when sending messages to his military commanders.
# We’ll call this number the encryption key. It is just the length of the shift we are using.
# For example, upon encrypting the message “cookie” using a shift cipher with encryption key 4, we obtain the encoded message (or ciphertext): GSSOMI.
# Let’s consider the following conversion table for English alphabets:&nbsp;
# Your challenge is to implement the above shift cipher in Python. You are expected to write two functions:

# • Encryption: An encryption function that takes the plain text and encryption key as an input and returns the ciphertext as output.

# • Decryption: This function will take the output and encryption key of the above encryption function and decode the message to give out the original plain text.

# Note: You are expected to handle only alphabetic inputs and white spaces for both your encryption and decryption functions.

def encryption(text: str, key: int):
    # ord and chr

    encrypted = ""

    for i in text: 
        if (text.isupper()):  

            encrypted += chr(((ord(i) - ord("A") + key) % 26) + ord("A"))
        else: 
            encrypted += chr(((ord(i) - ord("a") + key) % 26) + ord("a"))

    return encrypted


def decryption(text: str, key: int): 

    decrypted = ""

    for i in text: 
        if (text.isupper()):
            decrypted += chr(((ord(i) - ord("A") - key) % 26) + ord("A"))
        else:
            decrypted += chr(((ord(i) - ord("a") - key) % 26) + ord("a"))

    return decrypted

def main(): 
    assert(encryption("cookie", 4) == "gssomi")
    assert(decryption("gssomi", 4) == "cookie")
    
if __name__ == "__main__":
    main()
