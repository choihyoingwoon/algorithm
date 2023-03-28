from sys import stdin

result=[]
for i in range(3):
    n=int(stdin.readline())
    x=0
    for j in range(n):
        a=int(stdin.readline())
        x+=a
    if x>0:
        print('+')
    elif x==0:
        print('0')
    else:
        print('-')