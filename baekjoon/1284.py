while True:
    a=input()
    if int(a)==0:
        break
    x=len(a)+1
    for i in range(len(a)):
        if int(a[i])==1:
            x+=2
        elif int(a[i])==0:
            x+=4
        else:
            x+=3
    print(x)