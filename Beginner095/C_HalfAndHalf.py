A, B, C, X, Y = map(int, input().split())

if A <= C or B <= C:
  if X == min(X,Y):
    val = X * C * 2
    val = val + ((Y-X)*B)
  else:
    val = Y * C * 2
    val = val + ((X-Y)*A)

val_s = (A*X) + (B*Y)

if val > val_s:
  ans = val_s
else:
  ans = val

print(ans)
