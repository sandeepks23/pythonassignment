

words=input("Enter the words separated by commas")
lst=words.split(",")
lst1=sorted(lst)
for i in lst1:
    print(i,end=",")