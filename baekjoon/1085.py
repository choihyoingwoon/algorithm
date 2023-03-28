x,y,w,h=map(int,input().split())
a=1000
if a>x:
    a=x
if a>w-x:
    a=w-x
if a>y:
    a=y
if a>h-y:
    a=h-y
print(a)