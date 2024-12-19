from VotingModel.Blockchain import Blockchain


class PeerService:
    def __init__(self):
        self.blockchain: Blockchain = Blockchain()

    def getBlockChain(self):
        return self.blockchain

    def setBlockChain(self, blockchain: Blockchain):
        self.blockchain = blockchain
