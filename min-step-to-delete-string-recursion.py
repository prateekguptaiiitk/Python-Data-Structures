def helper(str, si, ei):
  if si > ei: return 0
     
  if ei - si + 1 == 1: return 1
 
  op1 = 1e9
  op2 = 1e9
  op3 = 1e9
 
  op1 = 1 + helper(str, si + 1, ei)
 
  if str[si] == str[si + 1]: 
    op2 = 1 + helper(str, si + 2, ei)
 
  for i in range(si+2, ei+1):
    if str[si] == str[i]:
      op3 = min(op3, helper(str, si + 1, i - 1) + helper(str, i + 1, ei))
 
  return min(op1, op2, op3)

def minStepToDeleteString(str):
  print(helper(str, 0, len(str)-1))

if __name__ == '__main__':
  minStepToDeleteString('2553432')
