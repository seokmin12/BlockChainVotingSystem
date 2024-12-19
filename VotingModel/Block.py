import time
from hashlib import sha256
from VotingModel.Transaction import Transaction


def apply_sha256(input):
    try:
        digest = sha256()
        digest.update(input.encode('utf-8'))
        hash_bytes = digest.digest()
        hex_string = ''.join(f'{b:02x}' for b in hash_bytes)
        return hex_string
    except Exception as e:
        print(e)
        raise RuntimeError(e)


class Block:
    def __init__(self, index, previous_hash, data):
        self.index: int = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.data: Transaction = data
        self.hash = self.compute_hash()
        self.valid: bool = False

    def compute_hash(self) -> str:
        calculatedHash = apply_sha256(
            self.previous_hash + str(self.timestamp) + str(self.index) + self.data.getTransactionId()
        )

        return calculatedHash

    def getIndex(self) -> int:
        return self.index

    def getTimestamp(self):
        return self.timestamp

    def getPreviousHash(self) -> str:
        return self.previous_hash

    def getHash(self) -> str:
        return self.hash

    def getData(self) -> Transaction:
        return self.data

    def setPreviousHash(self, previous_hash):
        self.previous_hash = previous_hash

    def setHash(self, hash):
        self.hash = hash

    def isValid(self) -> bool:
        return self.hash == self.compute_hash()

    def setValid(self, valid):
        self.valid = valid
