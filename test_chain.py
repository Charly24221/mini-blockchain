from chain import Blockchain
chain = Blockchain()
chain.add_block(["Arlo pays Tom 5"])
chain.add_block(["Tom pays Amy 3"])
chain.add_block(["Amy pays Arlo 1"])
assert chain.is_valid()==True, "区块添加失败"
b = Blockchain()
b.add_block(["Arlo pays Tom 5"])
b.add_block(["Tom pays Amy 3"])
b.add_block(["Amy pays Arlo 1"])
b.blocks[1].txs = ["Tom pays Amy 300"]
assert b.is_valid()==False,"区块篡改验证失败"
a = Blockchain()
a.add_block(["Arlo pays Tom 5"])
a.add_block(["Tom pays Amy 3"])
a.add_block(["Amy pays Arlo 1"])
a.blocks[0].txs = ["Tom pays Amy 300"]
assert a.is_valid()==False,"区块篡改验证2 失败"
assert b.blocks[1].prev_hash== b.blocks[0].calc_hash(),"区块链被篡改"
print("all test passed!")