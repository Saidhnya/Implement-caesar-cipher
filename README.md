This function takes two parameters:

ciphertext: The text encrypted using the Caesar Cipher.
shift: The number of positions each letter is shifted in the encryption process.
It iterates through each character in the ciphertext:

For each alphabetical character, it determines whether it is uppercase or lowercase and calculates the corresponding ASCII offset.
It applies the decryption shift to each character and constructs the plaintext.
Non-alphabetical characters are left unchanged.
Finally, it returns the decrypted plaintext.

In the example usage, it decrypts the text "Khoor Zruog" encrypted with a Caesar Cipher using a shift of 3. The decrypted text should be "Hello World".
