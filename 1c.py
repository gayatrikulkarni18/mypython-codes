v=int(input("\n Please Enter the Range number:"))
a=0
b=1
for n in range(0,v):
    if(n<=1):
        c=n
    else:
            c=a+b
            a=b
            b=c
    print(c)
