myDict={
    "Fast":"In a Quick Manner",
    "Saishna": "A Coder",
    "Marks" : [1 , 2 , 5 ],
    "anotherdict":{'harry':'Player'}
}
# print(myDict['Fast'])
# print(myDict['Saishna'])
# print(myDict['Marks'])
# print(myDict['anotherdict']['harry'])
# print(type(myDict.keys()))


#dictinory MAthods
print(list(myDict.keys())) #prints the keys of the dictionary
print((myDict.values())) #prints the values
print(myDict.items()) #printsthe keys,value for all th conatins of the dictinoary
print(myDict)
updateDict={
    "lovish":"Friend"
}
myDict.update(updateDict)  #updates the dictinoary by adding key-value in maindict
print(myDict)

print(myDict.get("saishna")) #get method will return none value

print(myDict["saishna"]) #throws an error as harry2 is nit present in the dic

print(myDict.get("harry")) #get method will return none value
print(myDict["harry2"]) #throws an error as harry2 is nit present in the dic