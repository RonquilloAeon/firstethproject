# See
# https://dev.to/gcrsaldanha/deploy-a-smart-contract-on-ethereum-with-python-truffle-and-web3py-5on
import json
import sys

from web3 import Web3

BLOCKCHAIN_URL = "http://127.0.0.1:7545"
COMPILED_CONTRACT = "build/contracts/HelloWorld.json"


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Missing contract address!")
        sys.exit(1)

    contract_address = sys.argv[1]

    web3 = Web3(Web3.HTTPProvider(BLOCKCHAIN_URL))
    web3.eth.defaultAccount = web3.eth.accounts[0]

    with open(COMPILED_CONTRACT, "r") as f:
        contract_json = json.load(f)
        abi = contract_json["abi"]

    contract = web3.eth.contract(contract_address, abi=abi)
    message = contract.functions.sayHello().call()
    print(message)

    tx_hash = contract.functions.setPayload("here i am").transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print(tx_hash.hex())
    print(tx_receipt)

    payload = contract.functions.payload().call()
    print("payload>", payload)
