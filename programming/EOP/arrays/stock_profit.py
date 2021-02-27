# Write a program that takes an array denoting the daily stock price, and returns the maximum profit that could be made by buying and then selling one share of that stock. There is no need to buy if no profit is possible.

def stock_profit(arr):
    global_min, max_profit = float('inf'), 0.0

    for ele in arr:
        temp_profit = ele - global_min
        max_profit = max(temp_profit, max_profit)
        global_min = min(global_min, ele)
    
    return max_profit

if __name__ == "__main__":

    prices = [190,310,310,230,340,390]

    max_profit = stock_profit(prices)

    print("Maximum profit %s"%max_profit)
        

        


