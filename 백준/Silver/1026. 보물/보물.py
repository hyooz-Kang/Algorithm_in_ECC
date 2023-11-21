n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
for i in range(n):
  a_t = min(a)
  b_t = max(b)
  s += a_t * b_t
  a.pop(a.index(a_t))
  b.pop(b.index(b_t))

print(s)