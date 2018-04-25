A, B, C, X, Y = map(int, input().split())

if A <= C or B <= C:
  if X == min(X,Y):
    val = X * C * 2
    val = val + ((Y-X)*B)
    print("X")
  else:
    val = Y * C * 2
    val = val + ((X-Y)*A)
    print("Y")
  print(val)

val_s = (A*X) + (B*Y)
print(val_s)

if val > val_s:
  ans = val_s
else:
  ans = val

print(ans)
