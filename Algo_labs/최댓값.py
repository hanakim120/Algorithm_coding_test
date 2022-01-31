import copy
num_list = []

for i in range(9):
  num_list.append(int(input()))

copy_array = copy.deepcopy(num_list)
copy_array.sort(reverse=True)
print(copy_array[0])
print(num_list.index(copy_array[0])+1)
