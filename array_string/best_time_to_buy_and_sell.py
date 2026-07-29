"""Problem Description
You are given an array prices where prices[i] represents the price of a stock on day i.

Your goal is to find the maximum profit you can make by:

Buying the stock on exactly one day
Selling the stock on a different day in the future (after the buy day)
You need to return the maximum profit possible from this single buy-sell transaction. If no profit can be made (for example, if prices only decrease), return 0.

Key constraints:

You must buy before you sell (the sell day must come after the buy day)
You can only make one transaction (one buy and one sell)
You cannot buy and sell on the same day"""



def buy_and_sell_solution(prices:list):

    min_price=99999999
    max_profit=0
    for price in prices:
        if price<min_price:
            min_price=price
        profit=price-min_price
        if profit>max_profit:
            max_profit=profit
    return max_profit

print("max_profit",buy_and_sell_solution([7, 6, 4, 3, 1]))
print("max_profit",buy_and_sell_solution([7, 1, 5, 3, 6, 4]))
print("max_profit",buy_and_sell_solution([7, 8,4,2,1,0,5,1,0,15,20]))


# Time complexity :O(n)
# Space Complexity :O(1)