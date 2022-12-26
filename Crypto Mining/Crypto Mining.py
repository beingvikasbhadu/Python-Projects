#Mining: It is a Process to guess the Nonce Value which gives hash value which starting with  X number of zeros
from hashlib import sha256
Max_Nonce=100000000000

def mine(block_number,transaction,previous_hash,prefix_zeros):
    prefix_str='0'*prefix_zeros
    for nonce in range(Max_Nonce):
        text=str(block_number)+transaction+previous_hash+str(nonce)
        current_hash=sha256(text.encode()).hexdigest()
        if current_hash.startswith(prefix_str):
            print(f"Yay! successfully mined bitcoin with nonce value: {nonce}")
            return current_hash
    raise BaseException(f"Couldn't find correct nonce value after trying {Max_Nonce} times")

if __name__=="__main__":
    transaction='''
    peter->zendya->80
    hulk->tony->100
    homelander->billy->200
    '''
    difficulty=4  #  try changing this to higher number and you will see it will take more time for mining as difficulty increases
    import time
    start=time.time()
    print("start mining: ")
    new_hash=mine(2,transaction,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7',difficulty)
    total_time=str(time.time()-start)
    print(f"Mining took: {total_time} second(s)")
    print(f"New Hash would be: {new_hash}")
