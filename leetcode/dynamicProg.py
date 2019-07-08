# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)
#
# output = []
# for number in range(int(name)):
#     #print("the number is: " + input())
#     # for i in range(1, int(input())):
#     #     p = [i]
#     # n = int(input())
#     factorial = 1
#     for n in range(1, int(input())+1):
#         # print(n)
#         factorial *= n
#     output.append(factorial)
# print(*output, sep = "\n")


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # you want to store the profit as key of an array
        states = []
        # for n in range(1, len(prices)):
        while len(prices) > 1:
            profits = []
            for n in range(1, len(prices)):
                profits.append(prices[n] - prices[0])
            # print(state)
            states.append(max(profits))
            prices.pop(0)

        return max(states)


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4])) # output 5