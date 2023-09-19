input_list = []
while(True):
  tmp_list = list(map(int, input().split()))
  if tmp_list == [0, 0, 0]:
    break
  else:
    input_list.append(tmp_list)

for i in range(len(input_list)):
  target = input_list[i]
  t_max = max(target)
  pop_target = target.copy()
  pop_target.pop(target.index(t_max))

  if sum(pop_target) <= t_max:
    print("Invalid")
  elif len(set(target)) == 3:
    print("Scalene")
  elif len(set(target)) == 2:
    print("Isosceles")
  elif len(set(target)) == 1:
    print("Equilateral")