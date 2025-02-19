import requests

# Polkadot Public RPC Endpoint
POLKADOT_RPC_URL = "https://polkadot-asset-hub-rpc.polkadot.io"

latest_block_hash = None  # Store the last seen block hash
waiting_for_new_block = False  # Flag to track if we're waiting for a new block

# JSON-RPC request to fetch the latest block hash
payload = {
    "jsonrpc": "2.0",
    "method": "chain_getBlock",
    "params": [],
    "id": 1
}

# Loop indefinitely
while True:
    try:
        # Make the request
        response = requests.post(POLKADOT_RPC_URL, json=payload).json()

        # Extract block details
        block = response["result"]["block"]
        block_number = int(block["header"]["number"], 16)  # Convert hex to decimal
        block_hash = block["header"]["parentHash"]

        # Print only if a new block is detected (different hash)
        if latest_block_hash != block_hash:
            print(f"\n🆕 New Block Detected!")
            print(f"Block Number: {block_number}")
            print(f"Block Hash: {block_hash}")

            latest_block_hash = block_hash  # Update the last seen block hash
            waiting_for_new_block = False  # Reset waiting flag
        else:
            # Only print "Waiting for new block" once
            if not waiting_for_new_block:
                print("Waiting for new block...")
                waiting_for_new_block = True  # Set flag to avoid printing again

    except Exception as e:
        print(f"⚠️ Error fetching block: {e}")
