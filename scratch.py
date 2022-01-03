import sys
import heapq

N = int(sys.stdin.readline().strip())

heap = list()
for _ in range(N):
    temp = list()
    q = int(sys.stdin.readline().strip())
    if q > 0:
        heapq.heappush(heap, (-q, q))
    elif q == 0:
        try:
            print(heapq.heappop(heap)[1])
        except IndexError: 
            print(0)
