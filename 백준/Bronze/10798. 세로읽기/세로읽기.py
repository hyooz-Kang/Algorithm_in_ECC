matrix = [[-1 for i in range(15)] for j in range(5)]
for i in range(5):
  tmp_word = list(input())
  tmp_len = len(tmp_word)
  matrix[i][:tmp_len] = tmp_word

res = ''

for j in range(15):
  for i in range(5):
    if(matrix[i][j] != -1):
      res += matrix[i][j]

print(res)