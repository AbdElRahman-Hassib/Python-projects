class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
    
    def __str__(self):
        return "Your rectangle dimensions are (Length:"+str(self.length)+" And width:"+str(self.width)+")"

class circle:
    def __init__(self,redius):
        self.redius=redius
    def area(self):
        return 3.14*self.redius*self.redius
    
class Editor:
    def __init__(self):
      self.rect=None
      self.circle=None

    def create_rectangle(self,length,width):
        self.rect=rectangle(length,width)

    def create_circle(self,redius):
        self.circle=circle(redius)

    def change_rectangle(self,factor):
        if self.rect == None:
            return
        self.rect.length,self.rect.width=self.rect.length+factor,self.rect.width+factor

    def change_circle(self,factor):
        if self.circle==None:
            return
        self.circle.redius=self.circle.redius+factor

    def print_area(self):
        if self.circle!=None:
            print("circle area="+str(self.circle.area()))
        if self.rect!=None:
            print("rect area="+str(self.rect.area()))


             
abcd=rectangle(5,2)
print(abcd.area())
print(abcd)
print(str(abcd))
print(abcd.__str__())
# m=circle(5)
# print(m.area())
# e=Editor()
# e.print_area()
# e.create_circle(1)
# e.create_rectangle(4,2)
# e.print_area()
# e.change_circle(2)
# e.print_area()
# e.change_rectangle(3)
# e.print_area()