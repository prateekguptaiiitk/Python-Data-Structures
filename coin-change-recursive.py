def count(coins, n, coin_sum):
  if (coin_sum == 0):
    return 1

  if (coin_sum < 0):
    return 0

  if (n <= 0):
    return 0

  return count(coins, n - 1, coin_sum) + count(coins, n, coin_sum-coins[n-1])

if __name__ == '__main__':
  coins = [1, 2, 3]
  coin_sum = 4
  print(count(coins, len(coins), coin_sum))
