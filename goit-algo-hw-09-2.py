import timeit

def find_min_coins(sum, coins):
    
    min_coins_required = [0] + [float('inf')] * sum    
    coin_used = [0] * (sum + 1)

    for i in range(1, sum + 1):
        for coin in coins:
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1                
                coin_used[i] = coin

    coins_count = {}

    current_sum = sum

    while current_sum > 0:
        coin = coin_used[current_sum]
        if coin in coins_count:
            coins_count[coin] += 1
        else:
            coins_count[coin] = 1
        current_sum -= coin

    return coins_count


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    sum = 113

print("Dynamic Programming Result:", find_min_coins(sum, coins))
dp_time = timeit.timeit(lambda: find_min_coins(sum, coins), number=1000)

print(f"Dynamic Programming Time: {dp_time:.10f} seconds")