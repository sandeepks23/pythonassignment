tup=(1,2,3,4,5,6,7,8,9,10)
lst=[]
even_tup=()
for i in tup:
    if i%2==0:
        lst.append(i)
even_tup=tuple(lst)
print(even_tup)