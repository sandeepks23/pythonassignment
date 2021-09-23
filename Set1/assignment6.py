class Circle:
    def __init__(self,radius):
        self.radius=radius

    def circle_area(self):
        area=3.14*self.radius*self.radius
        print("Area of the cirle is",area)

r=int(input("Enter the radius"))
obj=Circle(r)
obj.circle_area()