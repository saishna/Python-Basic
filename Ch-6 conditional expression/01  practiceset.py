# wap tofind the greatest of four number

a=int(input("enter 1st num"))
b=int(input("enter 2st num"))
c=int(input("enter 3st num"))
d=int(input("enter 4st num"))
if(a>=b and a>=c and a>=d):
    print("a is greatest")
elif(b>=c and b>=d):
    print("b is greates")
elif(c>=d):
    print("cis gretest")
else:
    print("d is greatest")

