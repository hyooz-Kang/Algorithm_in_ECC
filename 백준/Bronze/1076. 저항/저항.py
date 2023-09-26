color_dict = {'black':'0', 'brown':'1', 'red':'2', 'orange':'3', 'yellow':'4', 'green':'5', 'blue':'6', 'violet':'7', 'grey':'8', 'white':'9'}

c_list = []
for i in range(3):
  c_tmp = input()
  c_list.append(c_tmp)

c_1 = color_dict[c_list[0]]
c_2 = color_dict[c_list[1]]
c_3 = color_dict[c_list[2]]

print(int(c_1+c_2) * 10**(int(c_3)))