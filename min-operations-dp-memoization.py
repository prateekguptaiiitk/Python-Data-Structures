def minOperation(n, memo={}):
  if n in memo: return memo[n]
  if n == 1: return 1

  s = 0
  if n % 2 == 0:
    s += minOperation(n/2, memo) + 1
  else:
    s += minOperation(n-1, memo) + 1

  memo[n] = s
  return s

if __name__ == '__main__':
  print(minOperation(12))
