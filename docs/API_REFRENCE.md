## API Reference

### Python API

#### Federated Learning

##### FederatedTrainer
```python
from synark_os import FederatedTrainer

trainer = FederatedTrainer(
    model: str,                      # Model architecture name
    privacy_level: str,              # "standard", "hipaa", "high"
    blockchain_endpoint: str         # Blockchain RPC URL
)

# Methods
trainer.load_data(sources: List[str])  # Load training data
trainer.run(rounds: int, batch_size: int, **kwargs)  # Start training
trainer.get_model()  # Get trained model
```

#### Zero-Knowledge Proofs

##### ZKProver
```python
from synark_os.core import ZKProver

class ZKProver:
    def generate_proof(self, witness: bytes, public_inputs: bytes) -> bytes:
        """Generate zero-knowledge proof
        
        Args:
            witness: Serialized private inputs (protobuf format)
            public_inputs: SHA3-512 hash of public parameters
        
        Returns:
            PLONK proof with BLS12-381 curve
        """
        
    def verify(self, proof: bytes, public_inputs: bytes) -> bool:
        """Verify zero-knowledge proof"""