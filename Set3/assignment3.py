import re
x='[+][0-9]{1}[0-9]{1}\d{10}'
a=input("enter string")
matcher=re.finditer(x,a)
for match in matcher:
    print(match.group())
