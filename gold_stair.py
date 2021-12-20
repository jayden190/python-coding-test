def solution(n):
	if not n:
		return 0
	elif len(n) < 2:
		return n[0]
	elif len(n) == 2:
		return max(n[0], n[1])

	dp0 = n[0]
	dp1 = n[1]
	for i in range(2,len(n)):
		dp = max(dp0+ n[i], dp1)
		dp0,dp1 = dp1,dp
	return dp


def max_gold(n) -> int:
	prev1 = 0
	prev2 = 0
	cur = 0
	for i in n:
		cur = max(prev1, i + prev2)
		prev2 = prev1
		prev1 = cur
  	return cur

test1 = [1, 1, 1, 1, 1], 3
test2 = [1, 2, 10, 10, 3, 1], 14
test3 = [100, 1, 1, 1, 1, 1000], 1101
test4 = [1, 2, 10, 3, 1000, 10000], 10011
test5 = [1, 1], 1
test6 = [1], 1
test7 = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1], 4

tests = [test1, test2, test3, test4, test5, test6, test7]

if __name__ == '__main__':
	for i, test in enumerate(tests):
		ret = max_gold(test[0])
		print(i, test[1], ret, test[1] == ret)