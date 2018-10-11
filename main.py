from bitcash import Key
from bitcash.network import get_fee
import sys
import os

PRIVATE_KEY_PATH = "./private.secret"

def initialize():
    # print("making and saving new wallet...")
    key = Key()
    with open(PRIVATE_KEY_PATH,"w") as f:
        f.write(key.to_hex())

def load_key():
    with open(PRIVATE_KEY_PATH) as f:
        key = Key.from_hex(f.readline())
    return key
			

def main():
    #if len(sys.argv) < 2:
    #    return
    
    if not os.path.exists(PRIVATE_KEY_PATH):
        initialize()
    key = load_key()
    key.get_unspents()
    transaction_id = key.send(
        [],
        fee=get_fee("slow"),
        leftover=key.address,
        message=input(),
        #message=sys.argv[1],
        #unspents = key.unspents 
    ) 
    print(transaction_id)
     
		
if __name__=="__main__":
    main()

