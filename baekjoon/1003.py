def fibo_memo(x):
    if x == 0:
        memo[x] = [1,0]
        return memo[x]
    elif x == 1:
        memo[x] = [0,1]
        return memo[x]
    elif x in memo:
        return memo[x]
    else:
        a = fibo_memo(x-1)[0] + fibo_memo(x-2)[0]
        b = fibo_memo(x-1)[1] + fibo_memo(x-2)[1]
        memo[x] = [a,b]
        return memo[x]

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    memo = {}
    f = fibo_memo(n)
    print(f[0],f[1])