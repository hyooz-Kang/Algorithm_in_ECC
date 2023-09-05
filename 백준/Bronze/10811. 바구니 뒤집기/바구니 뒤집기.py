n,m = map(int, input().split(" "))
b_list = [i for i in range(1,n+1)]

for cnt in range(m):
  i, j = map(int, input().split(" "))
  tmp_list = b_list[(i-1):j]
  tmp_list.reverse()
  b_list[(i-1):j] = tmp_list

for k in range(n):
  print(b_list[k], end=" ")