values=input("Enter the numbers separated by comma")
lst=values.split(",")
lst1=[]
for i in lst:
    if int(i)%2!=0:
        lst1.append(int(i))

print(min(lst1))

