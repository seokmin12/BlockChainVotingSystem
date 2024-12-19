class ConsensusProtocol:
    def reachConsensus(self, blockchain):
        latestBlock = blockchain.getLatestBlock()
        previousBlock = blockchain.getPreviousBlock(latestBlock)

        if previousBlock is None:
            return True

        return previousBlock.getHash() == latestBlock.getPreviousHash()

    def validateBlock(self, block):
        hash = block.compute_hash()
        return hash == block.getHash()
