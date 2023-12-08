# A spam comment is defined as a text conataining following keywords:
# "make a lot of money", "buy now ", "susbscibe this",
# "click this", write a program to detect these spams.

text= input("enter a text")

if("make a lot of money"):
    spam=True
elif("buy now" in text):
    spam=True
elif("click this" in text):
    spam=True
elif("subscribe this" in text):
    spam=True
else:
    spam=False
if(spam):
    print("This text is spam")
else:
    print("This text is not spam")

