def minOperation(n):
  if n == 1: return 1

  s = 0
  if n % 2 == 0:
    s += minOperation(n/2) + 1
  else:
    s += minOperation(n-1) + 1

  return s

if __name__ == '__main__':
  print(minOperation(12))
