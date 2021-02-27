# Write a program that computes the maximum profit that can be made by buying and selling a share at most twice. The second buy must be made on another date after the first sale.

def buy_sell_twice(arr):

    if not arr:
        return 0

    max_profit, temp_min = 0, float('inf')
    first_buy_profits = [0]*len(arr)

    for i, ele in enumerate(arr):
        temp_min = min(temp_min, ele)
        max_profit = max(max_profit, ele - temp_min)
        first_buy_profits[i] = max_profit
    
    temp_max = float('-inf')
    for i, ele in reversed(list(enumerate(prices[1:], 1))):
        temp_max = max(temp_max, ele)
        max_profit = max(max_profit, temp_max - ele + first_buy_profits[i-1])
    
    return max_profit

if __name__ == "__main__":

    prices = [10,20,30,10,40,50,20]
    profit  = buy_sell_twice(prices)

    print ("max profit is %s"%profit)