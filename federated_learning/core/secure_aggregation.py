import torch
from lattice_cryptography import RingLWE, params

class HomomorphicAggregator:
    def __init__(self, model_dim, security_param=params.LWE_128):
        self.rlwe = RingLWE(security_param)
        self.public_key, self.private_key = self.rlwe.keygen()
        self.dim = model_dim
        
    def aggregate(self, encrypted_updates: list[bytes]) -> torch.Tensor:
        summed_c0 = torch.zeros(self.dim, dtype=torch.complex128)
        summed_c1 = torch.zeros(self.dim, dtype=torch.complex128)
        
        for ct in encrypted_updates:
            c0, c1 = self._deserialize_ciphertext(ct)
            summed_c0 = (summed_c0 + c0) % self.rlwe.modulus
            summed_c1 = (summed_c1 + c1) % self.rlwe.modulus
            
        return self.rlwe.decrypt((summed_c0, summed_c1), self.private_key)
    
    def _deserialize_ciphertext(self, data: bytes) -> tuple[torch.Tensor, torch.Tensor]:
        return (
            torch.frombuffer(data[:self.dim*8], dtype=torch.complex128),
            torch.frombuffer(data[self.dim*8:], dtype=torch.complex128)
        )