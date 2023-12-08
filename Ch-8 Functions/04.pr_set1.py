# Wap a number using function to find reatest of 3 numbers


def great(num1,num2,num3):
    if(num1>=num2 and num1>=num3):
        print("greatest",num1)
    elif(num2>=num3):
        print("greatest",num2)
    else:
        print("greatest",num3)

    great(22,33,44)
    # n1=int(input("enter 1st Number"))
    # n2=int(input("enter 2nd Number"))
    # n3=int(input("enter 3rd Number"))
    # great(n1,n2,n3)
    