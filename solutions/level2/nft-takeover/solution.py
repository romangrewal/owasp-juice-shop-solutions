from eth_account import Account

mnemonic_phrase = input("Enter mnemonic phrase: ")

Account.enable_unaudited_hdwallet_features()

account = Account.from_mnemonic(mnemonic_phrase)

private_key_bytes = account._private_key

private_key_hex = private_key_bytes.hex()

print("Mnemonic Phrase:", mnemonic_phrase)
print("Private Key (hex):", "0x" + private_key_hex)
print("Ethereum Address:", account.address)
