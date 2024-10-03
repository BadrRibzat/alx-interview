def makeChange(coins, total):
    # Return 0 if total is non-positive.
    if total <= 0:
        return 0
    
    # Return -1 if no coins are available.
    if len(coins) == 0:
        return -1
    
    # Sort coins for easier iteration.
    coins = sorted(coins)
    
    # Initialize DP array with 'inf' (no solution initially).
    dynamic = [float('inf')] * (total + 1)
    
    # Base case: 0 coins needed for total 0.
    dynamic[0] = 0
    
    # Iterate through each amount from 0 to total.
    for i in range(total + 1):
        for coin in coins:
            # Break if coin is larger than current amount.
            if coin > i:
                break
            # Update DP array if a valid solution exists.
            if dynamic[i - coin] != -1:
                dynamic[i] = min(dynamic[i - coin] + 1, dynamic[i])
    
    # Return -1 if no solution found, else return the minimum coins needed.
    return -1 if dynamic[total] == float('inf') else dynamic[total]
