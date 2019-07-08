# 1
# 4
# 2 2 3 7


# maximum = max(array)


# function for finding min
# operation
array = [2,2,3,7]

for i in range(len(array)):
    deleteStable = array.pop(i)
    array[i] = array[i] + 1

