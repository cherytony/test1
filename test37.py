import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print("队列大小：", q.qsize())
    print("队列元素", q.get())