def catalan(n, memo={}):
	if n in memo: return memo[n]
	if n <= 1: return 1

	res = 0
	for i in range(n):
		res += catalan(i, memo) * catalan(n-1-i, memo)

	memo[n] = res
	return res

for i in range(10): print(catalan(i), end=' ')
