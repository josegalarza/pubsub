import base64
import random
import string


UPPER_CASE=string.ascii_lowercase
LOWER_CASE=string.ascii_uppercase
DIGITS=string.digits
SPECIALS="~!@#$%^&*()_+`-=[]\\{}|;':\",./<>?"


class Cipher(object):
    """An instance of this class can:
        - generate keys
        - cipher/decipher messages based on the object's key
        - encode/decode base64 messages
    """


    def __init__(self, key=""):
        """Returns an instance object of this class"""
        self.key = key


    def cipher(self, message):
        """Ciphers and deciphers a message based on the object's key using the XOR method.

        Args:
            message (str): Message to cipher.

        Returns:
            ciphered (str): A ciphered version of the message.
        """
        tmpkey = self.key
        while len(tmpkey) < len(message):
            tmpkey += self.key
        ciphered = ''.join( [ chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(tmpkey, message) ] )
        return ciphered


    def generate_key(self, abecedary=UPPER_CASE + LOWER_CASE + DIGITS, size=64):
        """Generates a key, given an abecedary and a size.

        Args:
            abecedary (list): List of characters to generate the key from.
            size (int): Length of the key to generate.

        Returns:
            key (str): Key generated.
        """
        return ''.join(random.choice(abecedary) for _ in range(size))


    def encode_base64(self, bytes_or_str):
        """Base 64 encoder

        Args:
            bytes_or_str (bytes or string): Message to encode in base 64.

        Returns:
            output_bytes (bytes): Bytes encoded in base 64 for the argument.
        """
        if isinstance(bytes_or_str, str):
            input_bytes = bytes_or_str.encode("utf8")
        else:
            input_bytes = bytes_or_str
        output_bytes = base64.urlsafe_b64encode(input_bytes)
        return output_bytes
         # output_str = output_bytes.decode("utf8")
         # return output_str


    def decode_base64(self, bytes_or_str):
        """Base 64 decoder

        Args:
            bytes_or_str (bytes or string): Message to decode from base 64.

        Returns:
            output_bytes (bytes): Bytes decoded from base 64 for the argument.
        """
        output_bytes = base64.b64decode(bytes_or_str)
        return output_bytes
        # output_str = output_bytes.decode("utf8")
        # return output_str
