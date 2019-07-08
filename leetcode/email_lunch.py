# class Solution:
#     def numUniqueEmails(self, emails):
#         """
#         :type emails: List[str]
#         :rtype: int
#         """
#         count = 0
#         for i in emails:
#             for el in range(len(i)):
#                 if "@" in i[el]:
#                      if len(i[el:]) == 13:
#                          count += 1
#         return count
#
#
#
#
#
#
#
# sol = Solution()
# print(sol.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
#

# class Solution:
#     def findDiagonalOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         # twoLoops = [[i, j] for i in range(len(matrix)) for j in range(len(matrix[0]))]
#
#         """
#         traverse_diag = []
#
#         if not matrix: return traverse_diag
#
#         row = len(matrix)
#         col = len(matrix[0])
#
#         # avoid range and move smoothly
#         r_index = 0
#         c_index = 0
#
#         # while anything
#         while r_index < row and c_index < col:
#             traverse_diag.append(matrix[r_index][c_index])
#             if (r_index + c_index) % 2 == 0:
#                 # going up
#                 if c_index == col - 1:
#                     r_index += 1
#                 elif r_index == 0:
#                     c_index += 1
#                 else:
#                     r_index -= 1
#                     c_index += 1
#             else:
#                 # going down
#                 if r_index == row - 1:
#                     c_index += 1
#
#                 elif c_index == 0:
#                     r_index += 1
#                 else:
#                     r_index += 1
#                     c_index -= 1
#
#         return traverse_diag
#

#
# class Solution:
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         if len(matrix) == 1: return matrix
#         spiral = list()
#
#         for i in matrix[0]:
#             spiral.append(i)
#
#         for j in matrix[1:-1]:
#             spiral.append(j[-1])
#
#         for k in matrix[-1][::-1]:
#             spiral.append(k)
#
#         for l in matrix[1:-1][::-1]:
#             spiral.append(l[0])
#
#         # little_matrix = []
#         #
#         # for p in matrix[1:-1]: #[1:-1]:
#         #     little_matrix.append(p[1:-1])
#         # if not little_matrix:
#         #     return spiral
#         # else:
#         #     little_spiral = self.spiralOrder(little_matrix)
#         #     return spiral + little_spiral
#         for m in matrix[1:-1][0][1:-1]:
#             spiral.append(m)
#
#         return spiral
#
#
#
#
# mat = [
#  [ 1]
# ]
# mat2 = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [59, 86, 78, 88],
#   [9,10,11,12],
#     [9565,10454,15641,1462]
# ]
#
# sol = Solution()
# print(sol.spiralOrder(mat))

# 00 01 02
# 10 11 12
# 20 21 22
# n = [1,2,3,4,5]
# array_positive = [1,7,8,9,11,12]
#
# if 1 not in array_positive:
#     print(1)
# for i in n:
#     if i not in array_positive:
#         print(i)
#         break




# class Solution:
#     def transpose(self, matrix):
#
#         transpose_matrix = list()
#         for index in range(len(matrix[0])):
#             row = [i[index] for i in matrix]
#             transpose_matrix.append(row)
#
#         return transpose_matrix


# class Solution:
#     def searchInsert(self, nums, target):
#
#         # if not found reachinf the end
#         if len(nums) == 0:
#             return -1
#
#         left, right = 0, len(nums) - 1
#         while left < right:
#             mid = (left+right)//2
#             if target == nums[mid]:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid -1
#
#         return -1
#
#
# nums = [1,3,5,6,9]
# target = 6
# mattrix = [[5],[8]]
# sol = Solution()
# print(sol.searchInsert(nums, target))
#

# class Solution:
#     def square_binarySearch(self, number):
#
#         # return int(math.sqrt(x))
#         left, right = 0, number
#         while left <= right:
#             mid = (left+right)//2
#             if mid*mid == number:
#                 return mid
#             elif mid*mid < number:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#
#         return left - 1
#
import sys


# class Solution:
#
#     def input_number(self, look):
#         num = 10
#         if look == num: return 0
#         elif look < num: return 1
#         else:
#             return -1
#
#     def guess_number(self, my_guess):
#
#         if self.input_number(my_guess) == 0: return my_guess
#         left, right = 1, my_guess
#         while left  <= right:
#             mid = (left + right) // 2
#             status = self.input_number(mid)
#             if status == 0: return mid
#             elif status == 1:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#
#

# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#
#         left, right = 0, len(nums)-1
#         while left <= right:
#             mid = (left+right)//2
#             if nums[mid] == target: return mid
#             if target in nums[:mid]:
#                 return self.search(nums[:mid], target)
#             else:
#                 return self.search(nums[mid:], target)
#
#
# sol = Solution()
# print(sol.search([4,5,6,1,2,3], 1))

