f=open("test.txt")
data=[]
line_count=0
char_count=0
for lines in f:
    line_count+=1
    data+=lines.rstrip("\n").split(" ")
# print(data)
for i in data:
    for j in i:
        # print(j)
        char_count+=1

print("No.of lines:",line_count)
print("No.of words:",len(data))
print("No.of characters",char_count)