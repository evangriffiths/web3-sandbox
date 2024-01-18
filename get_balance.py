import dotenv
import os
from web3 import Web3

dotenv.load_dotenv()


def get_xdai(wallet_address: str, rpc: str):
    web3 = Web3(Web3.HTTPProvider(rpc))
    assert web3.is_connected()
    assert web3.net.version == "100"  # Gnosis Chain
    balance_wei = web3.eth.get_balance(wallet_address)
    return web3.from_wei(balance_wei, "ether")  # Actually xDai!!


if __name__ == "__main__":
    print(
        "xDai balance:",
        get_xdai(
            wallet_address=os.getenv("WALLET_ADDRESS"),
            # From https://chainlist.org/chain/100 -- need to connect wallet?
            rpc="https://endpoints.omniatech.io/v1/gnosis/mainnet/public",
        ),
    )
