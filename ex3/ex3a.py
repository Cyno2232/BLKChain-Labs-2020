from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
ex3a_txout_scriptPubKey = [OP_2DUP, OP_ADD, 1811,
                           OP_EQUALVERIFY, OP_SUB, 459, OP_EQUAL]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00100000
    txid_to_spend = (
        'd5495f17568e593a2775c93e32299ff218b0425e95adc4e9b079bcf34580eca8')
    utxo_index = 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex3a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)

# txid: 4497c8aaabfdc518a1221eadf3868ad595e8baf068b2fbbac3ab4a302a3e17d7