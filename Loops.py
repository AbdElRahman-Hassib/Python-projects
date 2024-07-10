num=int(input("Enter a number:"))
y,x =1,1
while y<=num:
    while x<=(num*2)-1:
        if x==num or num-(y-1)<=x<=num+y-1:
            print("*",end="")
        else:
            print(" ",end="")
        x=x+1
    print("")
    x=1
    y=y+1

y,x =1,1
while y<=num:
    while x<=(num*2)-1:
        if x==num or (x+y<=(2*num)and y<=x):
            print("*",end="")
        else:
            print(" ",end="")
        x=x+1
    print("")
    x=1
    y=y+1