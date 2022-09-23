def return_change(coin_types, change, min_coins, used_coins):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for i in [c for c in coin_types if c <= cents]:
            if min_coins[cents - i] + 1 < coin_count:
                coin_count = min_coins[cents - i] + 1
                new_coin = i
        min_coins[cents] = coin_count
        used_coins[cents] = new_coin
    return min_coins[change]


if __name__ == '__main__':
    n = int(input())
    coin_types = input().split()
    for i in range(n):
        coin_types[i] = float(coin_types[i])
        coin_types[i] = int(coin_types[i] * 100)
    received_value, purchase_value = input().split()
    received_value = float(received_value)
    purchase_value = float(purchase_value)
    change = received_value - purchase_value
    change = int(change * 100)
    min_coins = [0] * 100
    used_coins = [0] * 100
    return_change(coin_types, change, min_coins, used_coins)
    coin = change
    while coin > 0:
        this_coin = used_coins[coin]
        print("%.2f" % (this_coin / 100))
        coin = coin - this_coin
