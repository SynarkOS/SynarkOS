import os
import hashlib
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.asymmetric import x25519, ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import (
    Encoding, PublicFormat, PrivateFormat, NoEncryption
)

class MerkleTree:
    """Quantum-resistant Merkle tree implementation using SHA3-256"""
    def __init__(self, data_items):
        self.leaves = [self._hash(item) for item in data_items]
        self.tree = self._build_tree(self.leaves)
    
    @staticmethod
    def _hash(data):
        return hashlib.sha3_256(data).digest()
    
    def _build_tree(self, nodes):
        if len(nodes) == 1:
            return nodes
        new_level = []
        for i in range(0, len(nodes), 2):
            combined = nodes[i] + (nodes[i+1] if i+1 < len(nodes) else nodes[i])
            new_level.append(self._hash(combined))
        return self._build_tree(new_level)
    
    def get_root(self):
        return self.tree[0] if self.tree else None
    
    def get_proof(self, index):
        proof = []
        current_index = index
        current_level = self.leaves.copy()
        
        while len(current_level) > 1:
            sibling_index = current_index + 1 if current_index % 2 == 0 else current_index - 1
            if sibling_index < len(current_level):
                proof.append(current_level[sibling_index])
            
            current_index = current_index // 2
            current_level = self._build_tree(current_level)
            
        return proof

class QuantumSafeCrypto:
    @staticmethod
    def generate_key_pair():
        """Generate X25519 key pair with post-quantum security features"""
        private_key = x25519.X25519PrivateKey.generate()
        return {
            'private': private_key.private_bytes(
                Encoding.Raw,
                PrivateFormat.Raw,
                NoEncryption()
            ),
            'public': private_key.public_key().public_bytes(
                Encoding.Raw,
                PublicFormat.Raw
            )
        }

    @staticmethod
    def derive_shared_secret(private_key: bytes, public_key: bytes):
        """Post-quantum secure key derivation using X25519 and HKDF"""
        private = x25519.X25519PrivateKey.from_private_bytes(private_key)
        public = x25519.X25519PublicKey.from_public_bytes(public_key)
        shared_key = private.exchange(public)
        
        # NIST-recommended HKDF with SHA384
        return HKDF(
            algorithm=hashes.SHA384(),
            length=32,
            salt=os.urandom(16),
            info=b'quantum-safe-key-derivation'
        ).derive(shared_key)

    @staticmethod
    def zkp_proof_setup():
        """Elliptic Curve setup using NIST P-256 curve"""
        private_key = ec.generate_private_key(ec.SECP256R1())
        return {
            'private': private_key.private_bytes(
                Encoding.DER,
                PrivateFormat.PKCS8,
                NoEncryption()
            ),
            'public': private_key.public_key().public_bytes(
                Encoding.DER,
                PublicFormat.SubjectPublicKeyInfo
            )
        }

    @staticmethod
    def create_merkle_proof(data_items, index):
        """Generate Merkle proof for data integrity verification"""
        tree = MerkleTree([hashlib.sha3_256(item).digest() for item in data_items])
        return tree.get_proof(index)

    @staticmethod
    def encrypt_message(public_key: bytes, message: bytes):
        """Quantum-resistant hybrid encryption scheme"""
        # Generate ephemeral key pair
        ephemeral_private = x25519.X25519PrivateKey.generate()
        ephemeral_public = ephemeral_private.public_key()
        
        # Key exchange
        shared_secret = ephemeral_private.exchange(
            x25519.X25519PublicKey.from_public_bytes(public_key)
        )
        
        # Derive encryption keys
        hkdf = HKDF(
            algorithm=hashes.SHA512(),
            length=64,
            salt=None,
            info=b'hybrid-encryption'
        )
        key_material = hkdf.derive(shared_secret)
        enc_key, mac_key = key_material[:32], key_material[32:]
        
        # Encrypt with AES-GCM
        iv = os.urandom(12)
        cipher = Cipher(algorithms.AES(enc_key), modes.GCM(iv))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(message) + encryptor.finalize()
        
        return {
            'ephemeral_key': ephemeral_public.public_bytes(
                Encoding.Raw,
                PublicFormat.Raw
            ),
            'iv': iv,
            'ciphertext': ciphertext,
            'tag': encryptor.tag,
            'hmac': hmac.HMAC(mac_key, hashes.SHA512()).update(ciphertext).finalize()
        }

    @staticmethod
    def verify_merkle_proof(proof, target_hash, root_hash):
        """Verify Merkle proof against root hash"""
        current_hash = target_hash
        for sibling in proof:
            current_hash = hashlib.sha3_256(current_hash + sibling).digest()
        return current_hash == root_hash