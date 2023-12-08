b=set()
print(type(b))

# adding values to empty set
b.add(4)
b.add(4)
b.add(4) #adding the same value to set doesnt affect the set
# b.add([4,5,6]) #list is unhashable
# b.add((4,5,6)) #tuple can be added  
# b.add({4:5})
b.add(5)
print(b)

print(len(b)) #prints the length of this set
b.remove(5) #removes 5 from the set
# 
# b.remove(15) #throwa an error while removing 15 which is not present in the set
print(b)

print(b.pop())
print(b)

b.clear()
print(b)