## Installation Guide

### System Requirements
- **OS**: Ubuntu 22.04 LTS or later
- **GPU**: NVIDIA GPU with ≥ 8GB VRAM (Ampere+ recommended)
- **RAM**: 64GB minimum (128GB for large models)
- **Storage**: 500GB SSD
- **Optional**: Secure Enclave (Intel SGX/AMD SEV)

### Installation Steps

#### 1. Clone Repository
```bash
git clone https://github.com/yourusername/SynarkOS.git
cd SynarkOS
```

#### 2. Install System Dependencies
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3.10+
sudo apt install python3.10 python3-pip python3-venv

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

# Install Node.js and npm
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

#### 3. Install Python Dependencies
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install package
pip install -e .
```

#### 4. Build Rust Node Client
```bash
cd nodes/node_client
cargo build --release
cd ../..
```

#### 5. Setup Blockchain Environment
```bash
cd blockchain
npm install
npx hardhat compile
cd ..
```

#### 6. Configure IPFS (Optional)
```bash
# Install IPFS
wget https://dist.ipfs.io/go-ipfs/v0.14.0/go-ipfs_v0.14.0_linux-amd64.tar.gz
tar -xvzf go-ipfs_v0.14.0_linux-amd64.tar.gz
cd go-ipfs
sudo bash install.sh
ipfs init
ipfs daemon &
```

#### 7. Deploy with Docker
```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps
```

### Verification
```bash
# Test Python installation
python -c "import synark_os; print('SynarkOS installed successfully!')"

# Test Rust node
./nodes/node_client/target/release/synark-os-node --version

# Test blockchain connection
cd blockchain && npx hardhat test