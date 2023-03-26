def maxProd(n, memo={}):
  if n in memo: return memo[n]
  if n <= 1: return 0

  max_val = 0
  for i in range(1, n):
    max_val = max(max_val, (n-i)*i, maxProd(n-i, memo)*i)

  memo[n] = max_val
  return max_val

if __name__ == '__main__':
  print(maxProd(100))
