from brownie import SimpleStorage, accounts, config
from symbol import simple_stmt


def read_contract():
    simple_storage = SimpleStorage[-1]
    # Go take the idex that's one less than the length
    # ABI
    # Address
    print(simple_storage.retrieve())


def main():
    read_contract()
