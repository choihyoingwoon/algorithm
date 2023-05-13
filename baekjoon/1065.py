n=int(input())
if n<100:
    result=n
else:
    result=99
    for i in range(100,n+1):
        if int(str(i)[0])-int(str(i)[1])==int(str(i)[1])-int(str(i)[2]) or int(str(i)[2])-int(str(i)[1])==int(str(i)[1])-int(str(i)[0]):
            result+=1
print(result)