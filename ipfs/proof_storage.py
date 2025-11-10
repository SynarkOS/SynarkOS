# ipfs/proof_storage.py
import hashlib
import ipfshttpclient

class MerkleTree:
    """Custom Merkle tree implementation with BLAKE2"""
    def __init__(self, leaves):
        self.leaves = [self.hash(leaf) for leaf in leaves]
        self.root = self.build_tree(self.leaves)[0]
        
    @staticmethod
    def hash(data):
        return hashlib.blake2b(data, digest_size=32).digest()
    
    def build_tree(self, nodes):
        if len(nodes) == 1:
            return nodes
        new_level = []
        for i in range(0, len(nodes), 2):
            combined = nodes[i] + (nodes[i+1] if i+1 < len(nodes) else nodes[i])
            new_level.append(self.hash(combined))
        return self.build_tree(new_level)

class ProofManager:
    def __init__(self):
        self.client = ipfshttpclient.connect()
        self.tree = None

    def store_proofs(self, proofs):
        leaves = [self._hash_proof(p) for p in proofs]
        self.tree = MerkleTree(leaves)
        return self.client.add_json({
            "root": self.tree.root.hex(),
            "proofs": [self.client.add_bytes(p) for p in proofs]
        })

    def _hash_proof(self, proof):
        return hashlib.blake2b(proof, digest_size=32).digest()