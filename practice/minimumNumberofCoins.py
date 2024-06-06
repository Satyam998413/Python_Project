def min_coins(coins, amount):
    # Initialize dp array with a large number (infinity)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: No coins needed to make 0 amount
    
    # Update the dp array for each coin
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
coins = [1, 2, 5]
amount = 200
print(f"Minimum number of coins needed: {min_coins(coins, amount)}")