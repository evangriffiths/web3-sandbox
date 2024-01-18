from web3 import Web3


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
            wallet_address="0x3666DA333dAdD05083FEf9FF6dDEe588d26E4307",
            # rpc="https://lb.nodies.app/v1/68c917627d284b77888e2c90e9340862/",
            rpc="https://endpoints.omniatech.io/v1/gnosis/mainnet/public",
        ),
    )
