import time
from VotingModel.Block import Block
from VotingModel.Transaction import Transaction
from VotingModel.ConsensusProtocol import ConsensusProtocol


class Blockchain:
    def __init__(self):
        self.chain = []
        genesisBlock: Block = self.createGenesisBlock()
        self.chain.append(genesisBlock)

    def createGenesisBlock(self) -> Block:
        genesisTransaction: Transaction = Transaction("0", "Genesis Block")
        return Block(0, "0", genesisTransaction)

    def addBlock(self, block: Block):
        if ConsensusProtocol.validateBlock(block):
            self.chain.append(block)
        else:
            print("Invalid block. Consensus not reached.")

    def getPreviousBlock(self, block: Block) -> Block:
        index = block.getIndex()
        if 0 < index <= len(self.chain):
            return self.chain[index - 1]

    def getLatestBlock(self) -> Block:
        return self.chain[-1]

    def isValid(self) -> bool:
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]

            if not currentBlock.isValid():
                return False

            if currentBlock.getPreviousHash() != previousBlock.getHash():
                return False
        return True

    def setValid(self, valid: bool):
        self.valid = valid

    def getChain(self) -> [Block]:
        return self.chain

    def setLatestBlock(self, latestBlock: Block):
        self.latestBlock = latestBlock
