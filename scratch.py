import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

node = [[] for _ in range(N + 1)]

for _ in range(M):
  x, y = map(int, sys.stdin.readline().split())
  node[x].append(y)
  node[y].append(x)

count = 0
visited = [0 for _ in range(N + 1)]
def dfs(s):
  global count
  visited[s] = 1
  for i in node[s]:
    if not visited[i]:
      count += 1 
      dfs(i)
  
dfs(1)
print(count)

  