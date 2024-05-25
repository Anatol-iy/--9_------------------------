import timeit

def find_coins_greedy(sum, coins):
    coins = [50, 25, 10, 5, 2, 1]
    coins_count = {}
    
    for coin in coins:
        count = sum // coin
        if count > 0:
            coins_count[coin] = count
        sum -= coin * count             
    return coins_count

def find_coins_slow(sum, coins):
    coins_count = {}
    for coin in coins:
        while sum >=coin:
            sum -= coin
            coins_count[coin] = coins_count.get(coin, 0) + 1
    return coins_count

def find_coins_fast(sum, coins):
    coins_count = {}
    for coin in coins:
        count = sum // coin
        if count:
            coins_count[coin] = count
            sum %= coin
        if sum == 0:
            break
    return coins_count

if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    sum = 113

    # Використання функцій для обчислення решти
    print("Greedy Algorithm Result:", find_coins_greedy(sum, coins))
    print("Slow Algorithm Result:", find_coins_slow(sum, coins))
    print("Fast Algorithm Result:", find_coins_fast(sum, coins))

    # Порівняння часу виконання функцій

    greedy_time = timeit.timeit(lambda: find_coins_greedy(sum, coins), number=1000)
    slow_time = timeit.timeit(lambda: find_coins_slow(sum, coins), number=1000)
    fast_time = timeit.timeit(lambda: find_coins_fast(sum, coins), number=1000)

    print(f"Greedy Algorithm Time: {greedy_time:.5f} s")
    print(f"Slow Algorithm Time: {slow_time:.5f} s")
    print(f"Fast Algorithm Time: {fast_time:.5f} s")