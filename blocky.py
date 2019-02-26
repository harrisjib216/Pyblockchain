import sys
import hashlib as hasher
import datetime as date


# class
class Block:
    def __init__(self, index, date, obj, prev_hash):
        self.index = index
        self.date = date
        self.obj = obj
        self.prev_hash = prev_hash
        self.hash = self.new_block()

    def new_block(self):
        h256 = hasher.sha256()
        h256.update(
            str(self.index) + 
            str(self.date) + 
            str(self.obj) + 
            str(self.prev_hash)
        )
        return h256.hexdigest()



# mak
def init_block():
    return Block(0, date.datetime.now(), "Init Block", "0")



# get next/new block
def next_block(prev):
    this_index = prev.index + 1
    this_date = date.datetime.now()
    this_data = "Block " + str(this_index)
    this_hash = prev.hash
    return Block(this_index, this_date, this_data, this_hash)



#### BEGIN PROGRAM ####
future_blocks = sys.argv[1]
if not future_blocks:
    print "You need an argument!!!"
    sys.exit()



# build block chain
future_blocks = int(sys.argv[1])
chain = [init_block()]
prev_block = chain[0]



# Add blocks to the chain
for i in range(0, future_blocks):
  block_to_add = next_block(prev_block)
  chain.append(block_to_add)
  prev_block = block_to_add
  
  # results Tell everyone about it!
  print "Block #{} has been made".format(block_to_add.index)
  print "Hash: {}\n".format(block_to_add.hash) 