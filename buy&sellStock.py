# Leetcode 121

# Alogrithm:
# We need to evaluate what are the best days for buying and selling stock, i.e when will we make most profit. 
# For this, we can use two pointers, left and right at the starting two values
# We can initialise the max profit to be 0 initially.
# We can then calculate the profit for every left and right value and take the maximum of that and the existing maximum profit. 
# Then we can check if the left value is greater than the right value. If it is, this means we found a value lower than our current minimum value, in which case we can shift left to where right is. 
# Regardless of that, we shift right by 1 and we continue this loop while right is less than the length of the array. 
# We can then return the maximum profit. 

# Code:
def maxProfit(prices: list[int]) -> int:
    l,r = 0, 1
    maxProfit = 0
    while r < len(prices):
        maxProfit = max(maxProfit, prices[r]-prices[l])
        if prices[l] > prices[r]:
            l = r
        r += 1
    return maxProfit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,1,5,3,6,15]))
print(maxProfit([7,6,4,3,1]))

