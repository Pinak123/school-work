num=int(input("enter the number: "))
itter=[]
iterr=[]
def fibo(l):
    if l==0: return 0
    elif l==1: return 0
    elif l==2: return 1
    else:
        for i in range(l):
            curren=fibo(l-1)+fibo(l-2)
            itter.append(curren)

    return curren



def fibonacci(n):
    a=1
    b=1
    if n<=0: return 0
    if n==1: return 1
    if n==2: return 1
    else:
        for i in range(n-2):
            c=a+b
            a=b
            b=c
    return b

for i in range(num):
    print(fibonacci(i),end='')
    # print(i,end='')