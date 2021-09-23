class Test:
    def getString(self,c):
        self.c=c

    def printString(self):
        print(self.c.upper())

c=input("Enter string")
obj=Test()
obj.getString(c)
obj.printString()