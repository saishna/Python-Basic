# wap to fill in a letter template given below with name and date
letter='''Dear <|Name|>, 
You are selected!

Date:<|DATE|>'''

name=input("enter a name\n")
date=input("enter Date\n")
letter= letter.replace("<|Name|>",name)
letter= letter.replace("<|DATE|>",date)
print(letter)

