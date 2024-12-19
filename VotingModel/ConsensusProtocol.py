class ConsensusProtocol:
    @staticmethod
    def reachConsensus(blockchain) -> bool:
        latestBlock = blockchain.getLatestBlock()
        previousBlock = blockchain.getPreviousBlock(latestBlock)

        if previousBlock is None:
            return True

        return previousBlock.getHash() == latestBlock.getPreviousHash()

    @staticmethod
    def validateBlock(block) -> bool:
        hash = block.compute_hash()
        return hash == block.getHash()
