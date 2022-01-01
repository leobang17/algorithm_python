import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline().strip())
square = list()

for _ in range(N):
  square.append(list(map(int, sys.stdin.readline().split())))

blue_cnt = 0
white_cnt = 0

def recur(M, row_list, column_list):
  square_sum = 0
  global blue_cnt; global white_cnt
  for i in row_list:
    for j in column_list:
      square_sum += square[i][j] 
  if square_sum == M ** 2:
    blue_cnt += 1
  elif square_sum == 0:
    white_cnt += 1 
  else: 
    recur(M // 2, row_list[:M // 2], column_list[:M// 2])
    recur(M // 2, row_list[:M // 2], column_list[M// 2:])
    recur(M // 2, row_list[M // 2:], column_list[:M// 2])
    recur(M // 2, row_list[M // 2:], column_list[M// 2:])

recur(N, [i for i in range(N)], [i for i in range(N)])
print(white_cnt)
print(blue_cnt)