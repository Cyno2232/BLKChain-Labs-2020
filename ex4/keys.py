from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core import x

SelectParams('testnet')

######################################################################
# 
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cRaUQma9fHfs1bbf7ygZdrABA9riGMrBDWyxE1boryBXrkh8242P')
# Address:          mtWYPmR9FnGzYQ2jJWihNYQDMAEhVEENEA
# backcoinback:     mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB
# coin:             0.01021926
# txid:             309f44701640565c1a58abd210e6723d984f7a7710e081da280c5278edc9714a

# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cTqHpuUmFpGHCdWSnVVAJeUBzL28tWCxY2DpN6a1DDzpo5gmXZGv')
# Address:  miijP8xPSbyrgsXhoLhbcWnzp1dueP4UKt
# getcoin:  0.01232547
# txid:     dcacfaaedb28d27c3de731cc4d9e7ab3f33af3c3a275ef9e45943965cf9c096a

######################################################################
#
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=0b149be29c0847ce90d79ba0a26455be

# Send coins with 
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=<YOURTOKEN>

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('c3408bef2ba53e0c554ec161934e046e376fc162b57d36cc8ec7fd7eb0b6aeea'))
# "private": "c3408bef2ba53e0c554ec161934e046e376fc162b57d36cc8ec7fd7eb0b6aeea",
# "public": "03e5d1da20403dec1d0ac42f2f472e9a224e1eb3b182b63567704fbfdc617adc28",
# "address": "BzSQEcY6jmjXsdVAGKTJ9ML5avVe3tv1BD",
# "wif": "BusaKwQqMXj9ZCGAKfHtbuM7FcZvzd1MKav75q6PjMW5Qnu1byuw"

# Only to be imported by bob.py
# Bob should have coins!!
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=c35625ecbba9444ca8f1b8885d79d851
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('1b84362fdf6f618dd176fd0187fe59b4ea41838cfa35605775a5a03a8d2e1f32'))
#{
#  "private": "1b84362fdf6f618dd176fd0187fe59b4ea41838cfa35605775a5a03a8d2e1f32",
#  "public": "03bde3958f876c6e9ddd9b54e2608d419cc39b926a4617098321bf3e5468d6cc0f",
#  "address": "C5ApTWoBL72mgrXCXDULHDQrpCq1ysBD6i",
#  "wif": "BpFX4iQMvs7ptE4yfUZuvb4zesYyUjY4CpfgRVkZ4cEyyKdvFoZ2"
#}
#  "tx_ref": "cab354b01e9895f80c49b9e16bdbd0ec71de34b4451638c81286baea88e50368"


# Can be imported by alice.py or bob.py

alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)

alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
