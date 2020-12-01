######################################################################
# 区块链第一次作业 2020.11.07
# by 张倬玮 1811459 & 吕建瑶 1811400
# address: n1TfLmj1oZB9MD2f54XYmSxpoG1zQFMwzs
#######################################################################
from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cNLGdSSebyqLteVmucqngQ4KmmqZ2x6VLA7jDP7YUtfz3o38Q66H')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cUHvk3ZM6U5rn1cd2CJpbJvE941Jxrh6RRLMoQMvsp7jUEmNZmxj')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cPYtukzkHTibaPLFe3Jo9TfLLeDwGQWv9Rg5LNf3qbX2TBx1U3uS')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

ex2a_txout_scriptPubKey = [my_public_key, OP_CHECKSIGVERIFY, OP_1, cust1_public_key, cust2_public_key, cust3_public_key, OP_3, OP_CHECKMULTISIG]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0015
    txid_to_spend = (
        '78f73f3370fc4ec9a5d015d3ad40b69c9d918f88e310c08644c9a472857800f9')
    utxo_index = 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)

# txid 946b3104f54eb5485140117a461c073cb678d60c21a72573ab1f94705053b747