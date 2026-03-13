import hashlib
import time

# 区块类
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # 金融场景下：交易信息
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # 理解：所有字段参与哈希，确保任何修改都会改变 hash
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# 【任务】区块链类核心逻辑
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]#创造一个区块，是初始区块
        self.difficulty = 2  # 难度系数，控制前缀 0 的个数

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]#返回最新的一个区块

    # 任务 1：实现挖矿逻辑 (PoW)
    def mine_block(self, new_block) -> None:
        while True:
            current_hash = new_block.calculate_hash()
            if current_hash.startswith('0'*self.difficulty):
                new_block.hash = current_hash
                break
            else:
                new_block.nonce+=1
        self.chain.append(new_block)
        print(f"Block Mined! Hash: {new_block.hash}")

    # 任务 2：实现链的完整性验证
    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            # 检查点 1：当前区块的哈希值是否重新计算后一致？
            hash_now = self.chain[i].calculate_hash()
            if hash_now != self.chain[i].hash:
                return False
            # 检查点 2：当前区块的 previous_hash 是否指向上一个区块的真实哈希？
            if self.chain[i-1].hash != self.chain[i].previous_hash:
                return False
        return True

if __name__ == "__main__":
    my_coin = Blockchain()
    # 添加一笔交易
    new_tx = Block(1, time.time(), "A pays B $100", my_coin.get_latest_block().hash)
    my_coin.mine_block(new_tx)
    # 验证链
    print(f"Chain Valid? {my_coin.is_chain_valid()}") 
    # 尝试篡改
    my_coin.chain[1].data = "A pays B $1000000" 
    print(f"Chain Valid after tampering? {my_coin.is_chain_valid()}")