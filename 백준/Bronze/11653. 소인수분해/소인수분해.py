n = int(input())
cnt = 0
i_list = [i for i in range(2, int(n**0.5)+1)]
for i in i_list:
  while(n%i == 0):
    n /= i
    cnt += 1
    print(i)
if (n != 1):
  print(int(n))