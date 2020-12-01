from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

# TODO: Fill this in with your private key.
my_private_key = CBitcoinSecret(
    'cTD6cTXR4oCKWVC4F5c983kMMUynm3fdDn8bd3dxtHSYkThHhP2s')
my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)

faucet_address = CBitcoinAddress('moSy9Rigwgcg1UxYbQJ6joDx9VYVu69unZ')
