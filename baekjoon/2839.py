n=int(input())
b=5
s=3
result=n // b
while True:
    if (n-result*b)%s==0:
        result+=int((n-result*b)/s)
        break
    elif result==0 and n%s !=0:
        result=-1
        break
    else:
        result-=1
print(result)