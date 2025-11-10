# Contributing to SynarkOS

Thank you for your interest in contributing to SynarkOS!

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
   ```bash
   git clone https://github.com/yourusername/SynarkOS.git
   cd SynarkOS
   ```
3. **Create a branch** for your feature
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

1. Install dependencies (see `INSTALLATION.md`)
2. Run tests to verify setup
   ```bash
   pytest tests/
   cargo test --manifest-path nodes/node_client/Cargo.toml
   ```

## Contribution Guidelines

### Code Style
- **Python**: Follow PEP 8, use Black formatter
- **Rust**: Follow Rust conventions, use `rustfmt`
- **Solidity**: Follow Solidity style guide
- **Commits**: Use conventional commits format

### Pull Request Process

1. **Update tests** for your changes
2. **Update documentation** if needed
3. **Sign commits** with GPG (recommended)
4. **Create PR** with clear description
5. **Address review comments** promptly

### Testing

Run the full test suite:
```bash
# Python tests
pytest tests/ -v

# Rust tests
cd nodes/node_client && cargo test

# Smart contract tests
cd blockchain && npx hardhat test
```

## Security

### Vulnerability Reporting
Please report security vulnerabilities to: **synarkos@example.com**

- Do NOT open public issues for security vulnerabilities
- Include detailed reproduction steps
- We will respond within 48 hours

### Cryptographic Changes
Changes to cryptographic components require:
- Detailed security analysis
- Reference to relevant academic papers
- Review by maintainers

## Code of Conduct

- Be respectful and inclusive
- Follow open source best practices
- Help others learn and grow

## Questions?

Open a GitHub issue or contact the maintainers at synarkos@example.com