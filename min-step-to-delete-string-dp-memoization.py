def helper(str, si, ei, memo):
  if si > ei: return 0
     
  if ei - si + 1 == 1: return 1

  if memo[si][ei] != -1: return memo[si][ei]
 
  op1 = 1e9
  op2 = 1e9
  op3 = 1e9
 
  op1 = 1 + helper(str, si + 1, ei, memo)
 
  if str[si] == str[si + 1]: 
    op2 = 1 + helper(str, si + 2, ei, memo)
 
  for i in range(si+2, ei+1):
    if str[si] == str[i]:
      op3 = min(op3, helper(str, si + 1, i - 1, memo) + helper(str, i + 1, ei, memo))
 
  memo[si][ei] = min(op1, op2, op3)
  return min(op1, op2, op3)

def minStepToDeleteString(str):
  memo = [[-1 for i in range(len(str))] for j in range(len(str))]
  print(helper(str, 0, len(str)-1, memo))

if __name__ == '__main__':
  minStepToDeleteString('2553432')
