class my_range:
    def __init__(self, start, stop,step=1):
        self.start=start
        self.stop=stop
        self.step=step

    def has_next(self):
        if self.start<self.stop:
            return True
        else:
            return False

    def get_next(self):
        self.start+=self.step
        return self.start-self.step

r=my_range(1,11)

while r.has_next():
    print(r.get_next())

ra=my_range(1,11,3)

while ra.has_next():
    print(ra.get_next())

x=45
y=x
print(id(x))
print(id(y))
x=10
print(id(x))
print(id(y))
z=10
print(id(z))