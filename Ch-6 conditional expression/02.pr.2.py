# write a program to find out whether a student is pass or faiol if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user


a=int(input("enter a marks1"))
b=int(input("enter a marks2"))
c=int(input("enter a marks3"))
d=int(input("enter a marks4"))


total=a+b+c+d
if (a<33 or b<33 or c<33 or d<33):
    print("you are fail because yoy have less than 33% in one of the subjects")
if(total)/4<40:
    print("you are fail due to total percentage less than 40")
else: 
    print("you're passed")
    

