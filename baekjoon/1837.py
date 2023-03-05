p, k = map(int,input().split())
result=True
for i in range(2,k):
    if p%i ==0:
        print("BAD", i)
        result=False
        break
if result:
    print('GOOD')
