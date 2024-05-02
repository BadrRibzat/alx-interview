#!/usr/bin/python3
"""
Defining a function that determines a fewest number of coins to make change
"""


def makeChange(coins, total):
    """
    Determining the fewest numbers of coins needs to meet the given total

    parameters:
        coins [list or positive ints]:
            to give values of the coins in our possession
            we can assume that we have an infinite number of coins of all values
        total [int]:
            calculating the total amount of change to make
            if total is 0 or less, it should returns 0

    returns:
        -1 if the total change cannot be made with the given coins
    """
    if total <= 0:
        return 0
    if len(coins) is 0:
        return -1
    coins = sorted(coins)
    dynamic = [float('inf')] * (total + 1)
    dynamic[0] = 0
    for i in range(total + 1):
        for coin in coins:
            if coin > i:
                break
            if dynamic[i - coin] != -1:
                dynamic[i] = min(dynamic[i - coin] + 1, dynamic[i])
    if dynamic[total] == float('inf'):
        return -1
    return dynamic[total]
