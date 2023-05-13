

n=int(input())
for _ in range(n):
    a=int(input())
    zero=0
    one=0


    def fibonacci(n):
        if n == 0:
            print("0")
            zero += 1
        elif n == 1:
            print('1')
            one += 1
            return 1
        else:
            fibonacci(n - 1) + fibonacci(n - 2)

    if a==0:
        one+=1
    fibonacci(a)