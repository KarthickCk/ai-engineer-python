import threading
import time

chai_stock = 0

def restock_chai():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

threads = [threading.Thread(target=restock_chai) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final chai stock: {chai_stock}")