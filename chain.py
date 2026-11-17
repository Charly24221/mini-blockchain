import hashlib
class Block:
    def __init__(self,index,txs,prev_hash):
        self.index = index
        self.txs= txs
        self.prev_hash=prev_hash
    def calc_hash(self):
        text=f"{self.index}{self.txs}{self.prev_hash}"
        h = hashlib.sha256(text.encode()).hexdigest()
        return h

    def show(self):
        print(f"BLock{self.index}:{self.txs},{self.prev_hash},{self.calc_hash()}")
    def add_tx(self, tx):
        self.txs.append(tx)
class Blockchain:
    def __init__(self):
        self.blocks = []

    def add_block(self,txs):
        if len(self.blocks)==0:
            prev_hash=64*"0"
        else:
            prev_hash= Block.calc_hash(self.blocks[-1])
        index = len(self.blocks)+1
        new_block = Block(index,txs,prev_hash)
        self.blocks.append(new_block)

    def show_all(self):
        for b in self.blocks:
            b.show()

    def is_valid(self):
        for i in range(1,len(self.blocks)):
            if self.blocks[i].prev_hash!=self.blocks[i-1].calc_hash():
                return False
        return True

if __name__ == "__main__":
    chain = Blockchain()
    chain.add_block(["Arlo pays Tom 5"])
    chain.add_block(["Tom pays Amy 3"])
    chain.add_block(["Amy pays Arlo 1"])
    chain.show_all()

    print(chain.is_valid())
    chain.blocks[2].txs = ["Tom pays Amy 300"]
    print(chain.is_valid())
    chain.add_block(["Amy pays Arlo 1"])