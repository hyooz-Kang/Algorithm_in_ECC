alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
res_list = [ -1 for i in range(26)]

word = input()

for k in range(len(word)):
  target = word[k]
  idx = alphabet.index(target)
  if(res_list[idx] == -1):
    res_list[idx] = k

for i in range(26):
  print(res_list[i], end=" ")