import sys
from collections import deque
from copy import deepcopy

M, N = map(int, sys.stdin.readline().split())
tomato = list()
for _ in range(N):
  tomato.append(list(map(int, sys.stdin.readline().split())))
s = list()
for i in range(N):
  for j in range(M):
    if tomato[i][j] == 1:
      s.append(tuple([i, j]))

def bfs(s):
  q = deque(s)
  count = -1
  while q: 
    temp_q = deepcopy(q)
    q = deque()
    count += 1
    while temp_q: 
      x, y = temp_q.popleft()
      for i, j in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
        if i < 0 or j < 0: continue
        try:
          if tomato[i][j] == 0:
            tomato[i][j] = 1
            q.append(tuple([i, j]))
        except IndexError:
          pass

  for i in range(N):
    for j in range(M):
      if tomato[i][j] == 0:
        return -1
  return count

print(bfs(s))
  