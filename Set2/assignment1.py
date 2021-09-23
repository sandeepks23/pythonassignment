a=[]
users=input("Enter the users separated by commas")
a=users.split(",")
count=0
diff=0
if len(a)==1:
    for i in a:
        if i=="":
            print("Nobody likes This")
        else:
            print(i,"likes This")

elif len(a)==2:
    print(a[0],"and",a[1],"likes This")

else:
    diff=len(a)-2
    print(a[0], ",", a[1], "and", diff, "others like This")




