"""
This file implements the encryption and decryption function for the Vigenère Cypher
We don't use the Vigenère table but directly the mathematical principle
"""

import argparse
import random
import string


def encrypt(message, key, alphabet=string.ascii_uppercase):
    """Encrypt a message using Vigenère encryption.

    Args:
        message (string): message to encrypt. Should only contain characters from alphabet (+ eventual spaces)
        key (string): key for encryption. Should be at least as long as the message. Should only contain characters from alphabet.
        alphabet (list of chars, optional): alphabet of characters for message and key. Defaults to string.ascii_uppercase.

    Raises:
        Exception: raise exception when
            1. The key is shorter than the message OR
            2. The message uses a character that is not a space and not in the alphabet OR
            3. The key uses a character that is not in the alphabet.

    Returns:
        string: encrypted message
    """
    if len(key) < len(message):
        raise Exception("Key is shorter than message")

    encrypted_message = ""

    for i in range(len(message)):
        if " " not in alphabet and message[i] == " ":
            encrypted_message += " "
        else:
            if message[i] not in alphabet:
                raise ("Message uses a character not from the alphabet")
            elif key[i] not in alphabet:
                raise ("Key uses a character not from the alphabet")
            else:
                encrypted_message += alphabet[
                    (alphabet.find(message[i]) + alphabet.find(key[i])) % len(alphabet)
                ]
    return encrypted_message


def decrypt(message, key, alphabet=string.ascii_uppercase):
    """Decrypt a message using Vigenère encryption.

    Args:
        message (string): message to decrypt. Should only contain characters from alphabet (+ eventual spaces)
        key (string): key for decryption. Should be at least as long as the message. Should only contain characters from alphabet.
        alphabet (list of chars, optional): alphabet of characters for message and key. Defaults to string.ascii_uppercase.

    Raises:
        Exception: raise exception when
            1. The key is shorter than the message OR
            2. The message uses a character that is not a space and not in the alphabet OR
            3. The key uses a character that is not in the alphabet.

    Returns:
        string: decrypted message
    """
    if len(key) < len(message):
        raise Exception("key is shorter than message")

    decrypted_message = ""

    for i in range(len(message)):
        if " " not in alphabet and message[i] == " ":
            decrypted_message += " "
        else:
            if message[i] not in alphabet:
                raise ("Message uses a character not from the alphabet")
            elif key[i] not in alphabet:
                raise ("Key uses a character not from the alphabet")
            else:
                decrypted_message += alphabet[
                    (alphabet.find(message[i]) - alphabet.find(key[i])) % len(alphabet)
                ]
    return decrypted_message

def main():
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt string using Vigenère cypher"
    )
    parser.add_argument(
        "action",
        action="store",
        choices=["encrypt", "decrypt"],
        help="choose encryption or decryption",
    )
    parser.add_argument("message", help="message to encrypt or decrypt")
    parser.add_argument("key", help="should be at least as long as the message")
    args = parser.parse_args()
    if args.action == "encrypt":
        print(encrypt(args.message, args.key))
    else:
        print(decrypt(args.message, args.key))

if __name__ == "__main__":
    main()