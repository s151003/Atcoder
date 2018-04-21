import math

N, X = map(int, input().split())
m = {}
num = 0


for i in range(N):
  m[i] = int(input())
  X = X - m[i]
  num += 1

print(math.floor(X / min(m[i] for i in m) + num))
