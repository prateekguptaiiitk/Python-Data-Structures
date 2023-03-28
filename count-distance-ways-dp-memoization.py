def countWays(n, memo={}):
  if n in memo: return memo[n]
  if n < 0: return 0
  if n == 0: return 1

  memo[n] = countWays(n-1, memo) + countWays(n-2, memo) + countWays(n-3, memo)
  return memo[n]

if __name__ == '__main__':
  print(countWays(50))
