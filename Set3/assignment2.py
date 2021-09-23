import re
x='([a-zA-Z0-9_.+-]+@[a-zA-Z]+[.][a-zA-Z]+$)'
n=input("enter mail")
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")