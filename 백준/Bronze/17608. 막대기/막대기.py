from sys import stdin

n = int(stdin.readline())
stick = []

for i in range(n):
  tmp = int(stdin.readline())
  stick.append(tmp)

stick.reverse()

cnt = 1
top = stick[0]

for i in range(1,n):
  if top < stick[i]:
    top = stick[i]
    cnt += 1

print(cnt)