n = input()
cnt = 0
for i in range(1, len(n)):
  add = 9 * 10**(i-1) * i
  cnt += add
add_last = (int(n) - 10**(len(n)-1) + 1) * len(n)
cnt += add_last

print(cnt)