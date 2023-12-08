# wap to calculate the grade of a student from his marks from the schema

a=int(input('enter a maek1'))
b=int(input('enter a maek2'))
c=int(input('enter a maek3'))
d=int(input('enter a maek4'))
total=a+b+c+d
p=(total/5)*100
if(p>=90):
    print("excellent")
elif(p>=80 and p<=90):
    print("A")
elif(p>=70 and p<=80):
    print("b")
elif(p>=60 and p<=70):
    print("c")
elif(p<50):
    print("fail")

