def rangeSum(nums, i, j):
    # nums = [-2, 0, 3, -5, 2, -1]
    # those are index below
    # sumRange(0, 2) -> 1
    # sumRange(2, 5) -> -1
    # sumRange(0, 5) -> -3
    
    return sum(nums[i:j+1])