# Security Policy

## Supported Versions

| Version | Status | Quantum-Safe | Support Until |
|---------|--------|--------------|---------------|
| 1.0.x   | ✅ Active | ✅ Yes | 2030-12-31 |
| 0.x.x   | ⚠️ Beta | ✅ Yes | Best effort |

## Reporting a Vulnerability

If you discover a security vulnerability, please follow these steps:

### 1. **Do NOT** Open a Public Issue
Security vulnerabilities should never be disclosed publicly until they are resolved.

### 2. Report via Email
Send details to: **synarkos@example.com**

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### 3. Response Timeline
- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Resolution**: Varies by severity

### 4. Disclosure Policy
- We will coordinate disclosure timeline with you
- Public disclosure only after patch is released
- Credit will be given to reporters (unless anonymous)

## Security Features

### Cryptography
- **Post-Quantum**: NIST-approved algorithms (Kyber, Dilithium)
- **Encryption**: AES-256-GCM, X25519 key exchange
- **Hashing**: SHA3-256, BLAKE2b
- **ZK Proofs**: PLONK with BLS12-381 curve

### Privacy
- **Differential Privacy**: Configurable epsilon (ε < 1.0)
- **Secure Aggregation**: Homomorphic encryption (TFHE)
- **Zero-Knowledge**: No data leakage in proofs

### Infrastructure
- **TEEs**: Optional Intel SGX / AMD SEV support
- **TPM**: Hardware-backed key storage
- **Audit Logs**: Blockchain-immutable records

## Security Best Practices

### For Users
1. Always verify checksums of downloaded releases
2. Use hardware security modules when available
3. Keep dependencies updated
4. Enable differential privacy in production
5. Audit smart contracts before deployment

### For Contributors
1. Sign commits with GPG
2. Never commit secrets or keys
3. Follow secure coding guidelines
4. Run security tests before PR
5. Document cryptographic assumptions

## Third-Party Audits

We welcome independent security audits. Contact us to coordinate.

## Bug Bounty

Currently evaluating bug bounty program. Stay tuned!

## Contact

Security Team: synarkos@example.com