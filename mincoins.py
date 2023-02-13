def minimum_coins(change, denominations):
    num_coins = 0
    for coin in sorted(denominations, reverse=True):
        while change >= coin:
            change -= coin
            num_coins += 1
    return num_coins

denominations = [1, 2, 5, 10, 20, 50]
change = 43
print("Minimum number of coins required:", minimum_coins(change, denominations))
