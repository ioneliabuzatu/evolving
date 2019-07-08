def lis(nums):
    l = [1 for i in range(len(nums))]

    i = 1
    j = 0

    while i < len(nums):
        arr = nums[:i]
        for v in range(len(arr)):
            nv = nums[v]
            ni = nums[i]
            if nv < ni:
                l[i] = max(l[i], l[v]+1)

        i += 1

    return max(l)


print(lis([10, 9, 2, 5, 3, 7, 101, 18]))
