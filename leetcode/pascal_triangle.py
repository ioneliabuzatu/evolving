# n = 5
#
#
# def pascal(n):
#     output = []
#     while len(output) < n:
#             output.append([])
#     for l in output:
#         l.append(1)
#     for i in range(1, 5):
#         output[i].append(sum(output[i-1]))
#
#
#     return output
#
#
# print(pascal(n))

def removing(nums, val):
    # try:
    #     while True:
    #         nums.remove(val)
    #
    # except:
    #     return len(nums), nums
    nums.remove(val)
    return nums

print(removing(nums = [0,1,2,2,3,0,4,2], val = 2))
