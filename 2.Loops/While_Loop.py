ex_num=int(input("Enter the exercise number: "))
if ex_num==1:
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

    y =1
    x =1
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

elif ex_num==2:
    num=int(input("Enter a number:"))
    cntr=0
    while cntr<num:
        if cntr %8 ==0 or (cntr%3==0 and cntr %4 ==0):
            print(str(cntr)+" ")
        cntr+=1

elif ex_num==3:
    num=int(input("Enter a number:"))
    cntr=0
    while num>0:
        if cntr %3 ==0 and cntr %4 !=0:
            print(str(cntr)+" ",end="")
            num-=1
        cntr +=1

elif ex_num==4:
    num=int(input("Enter the number of test cases:"))
    while num>0:
        num2 = int(input("Enter how many numbers you wish to compare:"))
        first_time=1
        while num2>0:
            num3=int(input("Enter a number:"))
            if first_time:
                min_num=num3
                first_time=0
            if min_num>num3:
                min_num=num3
            num2-=1
        print("The minimum number is "+str(min_num))
        num-=1


elif ex_num==5:
    num=int(input("Enter a number of numbers you want to reverse:"))
    while num>0:
        num3 = 0
        num2=int(input("Enter a number you want to reverse:"))
        while num2>0:
            num3=num3*10+num2%10
            num2=num2//10
        print("reversed number is ",str(num3)+" multiplied by 3 :",str(num3*3))
        num-=1

elif ex_num==6:
    num,num2=map(int,input("Enter two number to print their multiplication table:").split())
    cntr1=1
    cntr2=1
    while cntr1<=num:
        cntr2=1
        while cntr2<=num2:
            print(str(cntr1)+"*"+str(cntr2)+"="+str(cntr1*cntr2))
            cntr2+=1
        cntr1+=1

elif ex_num==7:
    num=int(input("Enter the number of test cases:"))
    while num>0:
        num2 = int(input("Enter how many numbers:"))
        sum=0
        cntr=1
        while num2>0:
            num3=int(input("Enter a number:"))
            sum=sum+num3**cntr
            num2-=1
            cntr+=1
        print("result ="+str(sum))
    num+=1