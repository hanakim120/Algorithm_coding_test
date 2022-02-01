import copy

num_list = []

for i in range(9):
  num_list.append(int(input()))

copy_list = copy.deepcopy(num_list)
copy_list.sort()

print(copy_list[1])
print(num_list.index(copy_list[1])+1)
