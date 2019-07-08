# class Solution(object):
#     def findPeakElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         left, right = 0, len(nums) -1
#
#         while left < right:
#             mid = (left+right)//2
#             # if nums[mid+1] < nums[mid] > nums[mid-1]:
#             #     return mid
#
#             if nums[mid] > nums[mid+1]:
#                 right = mid
#             else:
#                 left = mid + 1
#
#         return left
#
#

class Solution(object):
    def findMin(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1






#nums = [3,2,1]
# nums = [4,5,6,7,0,1,2]
nums = [1,2,3,4,5,6,7,8,9]
sol = Solution()
print(sol.findMin(nums, 1))