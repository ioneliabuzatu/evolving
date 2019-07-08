def maxSub(array):
    out = []
    for el in range(1, len(array)):
       if array[el-1] > 0:
           array[el] += array[el-1]
    return max(array)


print(maxSub([-2,1,-3,4,-1,2,1,-5,4]))