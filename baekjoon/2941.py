word=input()
check=['c=','c-','dz=','d-','lj','nj','s=','z=']
result=[]
i=0
n=len(word)
while(i<=len(word)):
    for j in check:
        if word[i:len(j)+i] == j:
            result.append(j)
            i+=len(j)
            break
        elif word[i:len(j)+i] not in check and j=='z=':
            result.append(word[i-1])
            i += 1
    if (i>=len(word)):
        break

print(len(result))