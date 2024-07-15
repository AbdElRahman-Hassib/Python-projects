cntr=9
# for cntr in range(3,6,2):
#     print(cntr,end=" ")
# string="Hassib"
# for variable in string:
#     print(variable,end=" ")
Exercise_Num=int(input("Enter the exercise number:"))
if Exercise_Num ==1:
    TestCasesIndex=int(input("Enter the number of test cases:"))

    for i in range(0,TestCasesIndex):
        print("Test case index -> ",str(i+1))
        NumberOfInputs=int(input("Enter the number of inputs:"))
        Result=0
        for j in range(0,NumberOfInputs):
            number=int(input("Enter a number:"))
            temp1=1
            for k in range (1,j+2):
                temp1*=number
            Result+=temp1
            temp1=1
        print("Result = ",Result)

elif Exercise_Num ==2:
    n,m,SUM=map(int,input("Enter 3 numbers separated by space:").split())
    cntr=0
    for i in range (1,n+1):
        j=SUM-i
        if 1<=j<=m:
            cntr+=1
    print(cntr)

elif Exercise_Num ==3:
    n,m,w=map(int,input("Enter 3 numbers separated by space:").split())
    cntr=0
    for a in range(1,n+1):
        for b in range(a,m+1):
            for c in range(1,w+1):
                if a+b<=c:
                    cntr+=1
    print(cntr)

elif Exercise_Num ==4:
    n=int(input("Enter a number of lines to draw x:"))
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j or i+j==n+1:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

elif Exercise_Num ==5:
    cntr=0
    for x in range (50,301):
        for y in range(70,401):
            if x<y and ((x+y)%7) ==0:
                cntr+=1
            
    print(cntr)

elif Exercise_Num ==6:
    cntr=0
    for a in range (1,201):
        for b in range (1,201):
            for c in range (1,201):
                d=(a+b)-c
                if 1<=d<=200:
                    cntr+=1
    print(cntr)

elif Exercise_Num ==7:
    num=int(input("Enter a number to check if it's prime or not:"))
    Is_Prime=0
    for i in range(2,num):
        if num%i==0:
            Is_Prime=1
            break
    if Is_Prime:
        print("Not Prime")
    else:
        print("Prime")

elif Exercise_Num ==8:
    num=int(input("Enter a number to print all prime numbers before it:"))
    for i in range(2,num):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")

elif Exercise_Num ==9:
    n,a,b=map(int,input("Enter # numbers separated by a space").split())
    sum=0
    for i in range(1,n+1):
        x=i
        temp=0
        while x>0:
            temp+=x%10
            x=x//10
        if a<=temp<=b:
            sum+=i
    print(sum)
    
