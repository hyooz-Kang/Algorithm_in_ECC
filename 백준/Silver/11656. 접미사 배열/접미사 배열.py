text = input()
mylist = []

for i in range(len(text)):
  tmp = text[i:]
  mylist.append(tmp)

mylist.sort()

for i in range(len(mylist)):
  print(mylist[i])