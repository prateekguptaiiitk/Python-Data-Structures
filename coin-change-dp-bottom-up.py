def count(coins, n, coin_sum):
  table = [[0 for x in range(n)] for x in range(coin_sum+1)]

  for i in range(n):
    table[0][i] = 1

  for i in range(1, coin_sum+1):
    for j in range(n):
      x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0

      y = table[i][j-1] if j >= 1 else 0

      table[i][j] = x + y

  return table[coin_sum][n-1]

if __name__ == '__main__':
  coins = [1, 2, 3]
  coin_sum = 4
  print(count(coins, len(coins), coin_sum))
