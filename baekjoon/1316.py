n=int(input())
result=0
for _ in range(n):
    a=[]
    x=input()
    check=1
    k=0
    for i in x:
        if k != i and i in set(a):
            check=0
            break
        a.append(i)
        k=i
    if check==1:
        result+=1
print(result)
