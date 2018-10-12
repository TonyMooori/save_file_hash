from bitcash import Key
from bitcash.network import get_fee
import sys
import os

PRIVATE_KEY_PATH = "./private.secret"

def initialize():
    print("Making and saving new wallet...")
    key = Key()
    with open(PRIVATE_KEY_PATH,"w") as f:
        f.write(key.to_hex())
    print("Send some money to " + key.address)

def load_key():
    with open(PRIVATE_KEY_PATH) as f:
        key = Key.from_hex(f.readline().strip())
    return key
			

def main():
    if not os.path.exists(PRIVATE_KEY_PATH):
        initialize()
        return

    key = load_key()
    key.get_unspents()
    transaction_id = key.send(
        [],
        fee=1,
        leftover=key.address,
        message=input(),
    ) 
    print(transaction_id)
     
		
if __name__=="__main__":
    main()

