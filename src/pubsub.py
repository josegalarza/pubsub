import json
import time

from cipher import Cipher


class Message(object):


    def __init__(self, message):
        cipher = Cipher()
        self.message = cipher.encode_base64(message).decode()
        self.timestamp = time.time()


    def __str__(self):
        return json.dumps(
            {
                "message": self.message,
                "timestamp": self.timestamp,
            }
        )


class Topic(object):


    def __init__(self):
        cipher = Cipher()
        self.id = cipher.generate_key()
        self.messages = []
        self.pub_key = cipher.generate_key()
        self.sub_key = cipher.generate_key()


    def pub(self, message, pub_key):
        if self.pub_key == pub_key:
            message = Message(message)
            self.messages.append(message)
        else:
            raise RuntimeError("Unauthorized")


    def sub(self, sub_key):
        if self.sub_key == sub_key:
            try:
                message = self.messages.pop(0)
            except IndexError:
                message = ""
            return message
        else:
            raise RuntimeError("Unauthorized")


    def __str__(self):
        return json.dumps(
            {
                "id": self.id,
                "pub_key": self.pub_key,
                "sub_key": self.sub_key,
            }
        )
