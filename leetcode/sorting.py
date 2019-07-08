# def merge(n):
#
#     if len(n) == 1: return n
#
#     midpoint = len(n)//2
#     left = merge(n[:midpoint])
#     right = merge(n[midpoint:])
#
#     return mergesort(left, right)
#
# def mergesort(left,right):
#
#     out = []
#
#     l, r = 0, 0
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             out.append(left[l])
#             l += 1
#         elif right[r] < left[l]:
#             out.append(right[r])
#             r += 1
#
#     out += left[l:]
#     out += right[r:]
#
#     return out


# def mergeSort(x):
#     if len(x) < 2: return x
#     result = []
#     mid = int(len(x) / 2)
#     y = mergeSort(x[:mid])
#     z = mergeSort(x[mid:])
#     i = 0
#     j = 0
#     while i < len(y) and j < len(z):
#         if y[i] > z[j]:
#             result.append(z[j])
#             j += 1
#         else:
#             result.append(y[i])
#             i += 1
#     # result += y[i:]
#     # result += z[j:]
#     while i < len(y):
#         result.append(y[i])
#         i += 1
#
#     while  j < len(z):
#         result.append(z[j])
#         j += 1
#
#     return result

# print(mergeSort([5, 3, 7, 8, 1]))

def merge(intervals):

    

intervals = [[1,3],[2,6],[8,10],[15,18]]