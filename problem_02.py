# If you have a message you want to transmit securely, you can encrypt it (translate it into a secret code). One of the simplest ways to do this is with a shift cipher. Famously, Julius Caesar used this type of cipher when sending messages to his military commanders.
# We’ll call this number the encryption key. It is just the length of the shift we are using. For example, upon encrypting the message “cookie” using a shift cipher with encryption key 4, we obtain the encoded message (or ciphertext): GSSOMI.
# Let’s consider the following conversion table for English alphabets:&nbsp;
# Your challenge is to implement the above shift cipher in Python. You are expected to write two functions:

# • Encryption: An encryption function that takes the plain text and encryption key as an input and returns the ciphertext as output.

# • Decryption: This function will take the output and encryption key of the above encryption function and decode the message to give out the original plain text.

# Note: You are expected to handle only alphabetic inputs and white spaces for both your encryption and decryption functions.
