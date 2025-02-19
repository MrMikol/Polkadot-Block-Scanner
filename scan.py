import requests

# Polkadot Public RPC Endpoint
POLKADOT_RPC_URL = "https://polkadot-asset-hub-rpc.polkadot.io"

# JSON-RPC request to fetch the latest block hash
payload = {
    "jsonrpc": "2.0",
    "method": "chain_getBlock",
    "params": [],
    "id": 1
}

# Make the request
response = requests.post(POLKADOT_RPC_URL, json=payload).json()

# Extract block details
block = response["result"]["block"]
block_number = int(block["header"]["number"], 16)  # Convert hex to decimal
block_hash = block["header"]["parentHash"]

# Print the results
print(f"Block Number: {block_number}")
print(f"Block Hash: {block_hash}")
