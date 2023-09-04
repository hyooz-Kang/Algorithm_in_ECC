n = int(input())
n_point = 2
add = 1
for i in range(n):
  n_point += add
  add *= 2
res = n_point**2
print(res)