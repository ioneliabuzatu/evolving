def quicksort(nums):
    smaller = []
    equal = []
    greater = []
    if len(nums) > 1:
        pivot = nums[0]
        for num in nums:
            if pivot < num:
                greater.append(num)
            elif pivot == num:
                equal.append(num)
            else:
                smaller.append(num)

        return quicksort(smaller) + equal + quicksort(greater)
    return nums


def binary_search(sequence, num):
    first = 0
    last = len(sequence) - 1
    while first <= last:
        mid = (first + last) // 2
        if sequence[mid] < num:
            first = mid + 1
        elif num < sequence[mid]:
            last = mid - 1
        else:
            return mid
    return None


def binarysearch(sequence, value):
    lo, hi = 0, len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < value:
            lo = mid + 1
        elif value < sequence[mid]:
            hi = mid - 1
        else:
            return mid
    return None


sorted_seq = quicksort([3, 2, 5, 33, 77, 3, 1, 99])
print(binary_search(sorted_seq, 2))
print(binarysearch(sorted_seq, 2))
