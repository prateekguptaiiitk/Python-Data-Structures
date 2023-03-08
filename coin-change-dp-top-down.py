def coinchange(a, v, n, dp):
  if (v == 0):
    dp[n][v] = 1
    return dp[n][v]
  if (n == 0):
    return 0
  if (dp[n][v] != -1):
    return dp[n][v]
  if (a[n - 1] <= v):
    dp[n][v] = coinchange(a, v - a[n - 1], n, dp) + coinchange(a, v, n - 1, dp)
    return dp[n][v]
  else: 
    dp[n][v] = coinchange(a, v, n - 1, dp)
    return dp[n][v]

if __name__ == '__main__':
  tc = 1
  while (tc != 0):
    v = 4
    a = [1, 2, 3]
    dp = [[-1 for i in range(v+1)] for j in range(len(a)+1)]
    res = coinchange(a, v, len(a), dp)
    print(res)
    tc -= 1
