n=list(range(1,10001))
remove=[]
for i in n:
    num=int(i)
    for j in str(num):
        num+=int(j)
    if num<=10000:
        remove.append(num)
for i in set(remove):
    n.remove(i)
for i in n:
    print(i)