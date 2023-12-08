# wap to accept marks of 6 students and display them in a sorted manner
f1=int(input("enter a mark 1"))
f2=int(input("enter a mark 2"))
f3=int(input("enter a mark 3"))
f4=int(input("enter a mark 4"))
f5=int(input("enter a mark5"))
f6=int(input("enter a mark 6"))


markList=[f1,f2,f3,f4,f5,f6 ]
markList.sort()
print(markList)
