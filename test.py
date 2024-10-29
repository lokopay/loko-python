import time
import uuid

# 获取当前时间戳（以秒为单位）
timestamp = str(int(time.time()))

# 生成一个新的 UUID
nonce = str(uuid.uuid4())

print("Timestamp:", timestamp)
print("Nonce:", nonce)
