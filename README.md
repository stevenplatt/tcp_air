# TCP Air

A blockchain-based network access control system for OpenWRT devices.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Starting the Blockchain Node](#starting-the-blockchain-node)
  - [Registering Network Nodes](#registering-network-nodes)
  - [Adding Devices to the Network](#adding-devices-to-the-network)
  - [Consensus and Chain Validation](#consensus-and-chain-validation)
- [API Endpoints](#api-endpoints)
- [Security](#security)
- [License](#license)
- [Credits](#credits)

## Overview

TCP Air is a blockchain-based system designed to provide decentralized network access control for devices running OpenWRT. It uses a blockchain to maintain a ledger of authorized devices by their MAC addresses and automatically updates firewall rules on participating nodes.

The system is built on a simple proof-of-work blockchain implementation that allows network nodes to reach consensus on which devices are authorized to access the network. When a new device is added to the blockchain, all participating nodes update their firewall rules to allow traffic from that device.

## Features

- Blockchain-based network access management
- Automatic firewall rule generation for OpenWRT devices
- Self-signed SSL/TLS support for secure communication
- REST API for blockchain interaction
- Consensus mechanism for resolving conflicts between nodes
- MAC address-based device authorization

## Requirements

- Python 3.x
- OpenWRT-based router or device
- Additional Python packages:
  - Flask
  - Requests
- CURL (for testing API endpoints)

## Installation

1. Clone this repository to your OpenWRT device
2. Run the installer script:

```
python installer.py
```

This will create the necessary directory structure at `/etc/config/tcp_air/` and copy the required files.

## Usage

### Starting the Blockchain Node

The main blockchain implementation is contained in `network_chain.py`. To start a blockchain node:

```
python network_chain.py
```

This will start a Flask server on port 5000 (or port 5001/5002 if using `network_chain2.py` or `network_chain3.py`) with SSL enabled using the included self-signed certificates.

### Registering Network Nodes

To register other blockchain nodes with your node, send a POST request to the `/nodes/register` endpoint:

```
curl -X POST -H "Content-Type: application/json" -d '{"nodes": ["https://192.168.1.2:5000"]}' https://localhost:5000/nodes/register --insecure
```

### Adding Devices to the Network

To add a new device to the network, create a new transaction with the device's MAC address:

```
curl -X POST -H "Content-Type: application/json" -d '{"sender": "your_node_id", "recipient": "device_id", "mac": "AA:BB:CC:DD:EE:FF", "action": "add device", "amount": 1}' https://localhost:5000/transactions/new --insecure
```

This will create a new transaction, mine a new block containing that transaction, and update the firewall rules on the node.

### Consensus and Chain Validation

The system uses a simple Proof of Work consensus algorithm and longest chain rule to resolve conflicts. To manually trigger consensus resolution:

```
curl -X GET https://localhost:5000/nodes/resolve --insecure
```

## API Endpoints

- `GET /chain` - Retrieve the full blockchain
- `GET /mine` - Mine a new block
- `POST /transactions/new` - Create a new transaction
- `POST /nodes/register` - Register new nodes
- `POST /nodes/remove` - Remove registered nodes
- `GET /nodes/resolve` - Resolve conflicts using consensus

## Security

The current implementation uses self-signed certificates for SSL/TLS. In production, valid certificates should be used. The system also disables certificate verification in the `resolve_conflicts` method, which should be fixed in a production deployment.

**Note:** The current implementation is meant for testing and development purposes. Additional security measures would be needed for a production environment.

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

The blockchain implementation is partially based on example code by Daniel van Flymen:
https://hackernoon.com/learn-blockchains-by-building-one-117428612f46