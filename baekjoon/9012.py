n=int(input())
for _ in range(n):
    x=input()
    check=[]
    num=0
    for i in x:
        if i == '(':
            check.append(i)
        elif len(check)>0 and i == ')':
            check.pop(len(check)-1)
        elif len(check) == 0 and i == ')':
            num=1
            break
    if num==1:
        print("NO")
    else:
        if len(check)==0:
            print('YES')
        else:
            print('NO')