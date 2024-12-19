from VotingModel.Blockchain import Blockchain
from VotingModel.Transaction import Transaction
from VotingModel.Block import Block
from VotingModel.ConsensusProtocol import ConsensusProtocol

from hashlib import sha256
from collections import defaultdict
from typing import List, Dict


class VotingSystem:
    def __init__(self):
        self.blockchain: Blockchain = Blockchain()
        self.candidate_votes = defaultdict(int)
        self.candidates = ["Candidate1", "Candidate2", "Candidate3", "Candidate4"]

    def set_blockchain(self, blockchain: Blockchain):
        self.blockchain = blockchain
        self.synchronize_candidate_votes()

    def cast_vote(self, voter_id: str, candidate: str, private_key, public_key):
        if self.has_voted(voter_id):
            print("You have already cast your vote.")
            return

        if not self.is_valid_candidate(candidate):
            print("Invalid candidate.")
            return

        transaction: Transaction = Transaction(voter_id, candidate)
        transaction.generateSignature(private_key)

        if not transaction.verifySignature(public_key):
            print("Invalid transaction signature.")
            return

        new_block: Block = Block(self.blockchain.getLatestBlock().index + 1,
                                 self.blockchain.getLatestBlock().hash, transaction)

        if ConsensusProtocol.reachConsensus(self.blockchain):
            self.blockchain.addBlock(new_block)
            self.update_candidate_votes(candidate)
            print("Casted vote successfully!")
        else:
            print("Consensus not reached. Vote not cast.")

    def update_candidate_votes(self, candidate: str):
        self.candidate_votes[candidate] += 1

    def synchronize_candidate_votes(self):
        self.candidate_votes.clear()
        for block in self.blockchain.getChain():
            transaction = block.getData()
            if transaction is not None and transaction.getCandidate() != "Genesis Block":
                candidate = transaction.getCandidate()
                self.candidate_votes[candidate] += 1

    def has_voted(self, voter_id: str) -> bool:
        for block in self.blockchain.getChain():
            transaction = block.getData()
            if transaction is not None and transaction.getVoterId() == voter_id:
                return True
        return False

    def verify_hash(self, voter: str, hashed_data: str) -> bool:
        hashed_voter = self.bytes_to_hex(sha256(voter.encode('utf-8')).digest())
        return hashed_voter == hashed_data

    def bytes_to_hex(self, bytes_data: bytes) -> str:
        return ''.join(f'{b:02x}' for b in bytes_data)

    def is_valid_candidate(self, candidate: str) -> bool:
        return candidate in self.candidates

    def get_chain(self) -> List:
        return self.blockchain.getChain()

    def calculate_results(self) -> Dict[str, int]:
        return dict(self.candidate_votes)

    def get_candidates(self) -> List[str]:
        return self.candidates
