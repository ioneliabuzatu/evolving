def houses(nums):
    current = 0
    past = 0

    for cur in nums:
        past, current = current, max(past+cur, current)

    return current


print(houses([2,7,9,3,1]))

