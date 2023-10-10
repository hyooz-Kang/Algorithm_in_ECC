def isSosu(num):
  flag = 0
  for i in range(2, num):
    tmp = num % i
    if tmp == 0:
      flag += 1

  if flag == 0:
    res = 1
  else:
    res = 0

  return res


n = int(input())
num_list = list(map(int, input().split()))

cnt = 0

for i in range(n):
  target = num_list[i]
  if target > 2:
    res = isSosu(target)
    cnt += res
  elif target == 2:
    cnt += 1

print(cnt)