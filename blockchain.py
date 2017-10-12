import hashlib
import json
from time import time

class Blockchain(object):
	def __init__(self):

		# Create private variables
		# chain: array of blocks in the entire blockchain
		# current_transactions: array of transaction objects to be included in next block
		self.chain = []
		self.current_transactions = []

		# Create the genesis block
		self.new_block(previous_hash = 1, proof = 100)

	def new_block(self, proof, previous_hash=None):
		"""
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

		block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

	def new_transaction(self):
		# TODO
		pass

	@staticmethod
	def hash(block):
		"""
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

	@property
	def last_block(self):
		return self.chain[-1]

	def new_transction(self, sender, recipient, amount):
		"""
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        
		self.current_transactions.append({
			'sender': sender,
			'recipient': recipient,
			'amount': amount
			})
		return self.last_block['index'] + 1

