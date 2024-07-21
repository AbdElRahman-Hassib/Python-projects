def print_menu():
    flag=False
    while flag==False:
        number=int(input("Enter a number from 1 to 3:\n1:sum all numbers from 1 to N\n2:Division\n3:Enter a mathimatical exepression\n"))
        if number==1 or number==2 or number==3:
            flag=True
            return number
        else:
            print("invalid input")

def sum_1_to_N():
    number=int(input("Enter a number to sum from 1 to N:"))
    sum=0
    for i in range(1,number+1):
        sum+=i
    print(sum)  

def division():
    number1,number2=map(int,input("Enter two number for division separated by space:").split())
    if number2==0:
        print("Can't divide by ZERO")
    else:
        print(number1/number2)

def Exepression():
    number1,operator,number2=input("Enter a mathimatical exepression separated by space:").split()
    if operator=="+":
        print(str(number1)+"+"+str(number2)+"="+str(int(number1)+int(number2)))
    elif operator=="-":
        print(str(number1)+"-"+str(number2)+"="+str(int(number1)-int(number2)))
    elif operator=="*":
        print(str(number1)+"*"+str(number2)+"="+str(int(number1)*int(number2)))
    elif operator=="/" and int(number2)!=0:
        print(str(number1)+"/"+str(number2)+"="+str(int(number1)/int(number2)))
    elif operator=="/" and int(number2)==0:
        print("Can't divide by ZERO")
    else:
        print("invalid operator")

def calculatror_interface():
    number=print_menu()
    if number==1:
        sum_1_to_N()
    elif number==2:
        division()
    elif number==3:
        Exepression()
    else:
        print("invalid input")


calculatror_interface()


