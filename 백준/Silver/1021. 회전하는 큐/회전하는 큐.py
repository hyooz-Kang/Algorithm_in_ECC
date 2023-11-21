from collections import deque

n, m = map(int, input().split())
myindex = list(map(int, input().split()))

queue = deque([i for i in range(1, n+1)])

cnt = 0

for i in range(m):
  while True:
    if queue[0] == myindex[i]:
      queue.popleft()
      break
    else:
      if queue.index(myindex[i]) < len(queue)/2 :
        while queue[0] != myindex[i]:
          queue.append(queue.popleft())
          cnt += 1
      else:
        while queue[0] != myindex[i]:
          queue.appendleft(queue.pop())
          cnt += 1

print(cnt)