n = int(input())
grade_list = list(map(int, input().split()))
m = max(grade_list)

change_list = []
for i in range(n):
  change_list.append((grade_list[i] / m) * 100)

new_avg = sum(change_list) / n

print(new_avg)