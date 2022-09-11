def revnum(num):
    sum=0
    while num!=0:
        rem =num%10
        sum=rem+sum*10
        num=num//10
        print("Reverse num:%d"%sum)
num=int(input("Enter any number:"))
revnum(num)
