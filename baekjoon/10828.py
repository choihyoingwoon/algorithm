import sys
n=int(sys.stdin.readline())
array=[]
for _ in range(n):
    a=sys.stdin.readline().split()
    if a[0]=="push":
        array.append(a[1])
    else:
        if a[0]=='pop':
            if len(array)==0:
                print(-1)
            else:
                print(array.pop())

        elif a[0]=='size':
            print(len(array))
        elif a[0]=='empty':
            if len(array)==0:
                print(1)
            else:
                print(0)
        else:
            if len(array)==0:
                print(-1)
            else:
                print(array[-1])

