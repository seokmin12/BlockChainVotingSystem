from hashlib import sha256
import rsa


class Transaction:
    def __init__(self, voterId, candidate):
        self.voterId: str = voterId
        self.candidate: str = candidate
        self.transactionId: str = self.calculateTransactionId()
        self.signature: [bytes] = None

    def calculateTransactionId(self):
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

    def verifySignature(self, public_key):
        data = self.voterId + self.candidate + self.transactionId
        try:
            verify = rsa.verify(data, self.signature, public_key)
            print(verify)
            return True
        except (ValueError, TypeError) as e:
            print(e)
        return False

    def getVoterId(self):
        return self.voterId

    def getCandidate(self):
        return self.candidate

    def getTransactionId(self):
        return self.transactionId
