def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}

    for i, n in enumerate(nums):
        if n in dict:
            return [dict[n], i]
        dict[target - n] = i

print(twoSum([3,2,4,9], 13))