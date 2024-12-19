from hashlib import sha256
import rsa


class Transaction:
    def __init__(self, voterId, candidate):
        self.voterId: str = voterId
        self.candidate: str = candidate
        self.transactionId: str = self.calculateTransactionId()
        self.signature: [bytes] = None

    def calculateTransactionId(self) -> str:
        data: str = self.voterId + self.candidate
        try:
            hash: [bytes] = sha256(data.encode()).hexdigest()
            return hash
        except TypeError or UnicodeError as e:
            print(e)

        return None

    def generateSignature(self, private_key):
        data: str = self.voterId + self.candidate + self.transactionId
        try:
            signature = rsa.sign(data.encode(), private_key, 'SHA-256')
            self.signature = signature
        except Exception as e:
            print(e)

        return None

    def verifySignature(self, public_key) -> bool:
        data: str = self.voterId + self.candidate + self.transactionId
        try:
            rsa.verify(data.encode('utf-8'), self.signature, public_key)
            return True
        except (ValueError, TypeError) as e:
            print(e)
        return False

    def getVoterId(self) -> str:
        return self.voterId

    def getCandidate(self) -> str:
        return self.candidate

    def getTransactionId(self) -> str:
        return self.transactionId
