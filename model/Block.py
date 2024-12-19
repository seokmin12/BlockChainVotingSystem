from hashlib import sha256
import json
import time


class Block:
    def __init__(self, index, timestamp, previousHash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
