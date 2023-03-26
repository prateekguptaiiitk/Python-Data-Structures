def minCoins(V, coins, memo={}):
  if V in memo: memo[V]
  if V == 0: return 0
  minn = float('inf')

  for coin in coins:
    if V >= coin:
      rem = minCoins(V-coin, coins, memo) + 1

      if rem < minn:
        minn = rem

  memo[V] = minn
  return minn

if __name__ == '__main__':
  print(minCoins(39, [9, 2, 11, 5, 14, 17, 8, 18]))
