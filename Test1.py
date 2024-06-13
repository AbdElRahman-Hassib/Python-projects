"""
first_num,second_num=map(float,input("enter two numbers:").split())
print(type(first_num))
print((second_num))
print(str(first_num)+"+"+str(second_num)+"=",first_num+second_num)
print(str(first_num)+"-"+str(second_num)+"=",first_num-second_num)
print(str(first_num)+"*"+str(second_num)+"=",first_num*second_num)
print(str(first_num)+"/"+str(second_num)+"=",first_num/second_num)
"""
"""""
a,b,c=map(int,input("enter three numbers:").split())

temp=a
a=b
b=c
c=temp

print(a,b,c)
"""
"""
print(7 or 5)
name= "hassib"
print("assib"in name)
print("ib"in name)
print("has"in name)
print("ab"in name)
print("hassib"in name)
"""
#check if the number is even by 3 different ways

num=int(input("Enter your number to check if it's even: "))

IsEven_1=num%2==0
IsEven_2=(num/2-num//2)==0
IsEven_3=(not(num%10&1))
print("The result is "+str(IsEven_1)+str(IsEven_2)+str(IsEven_3))

isodd=not IsEven_1

form=100 *IsEven_1 +7*isodd
print("The result is "+str(form) )
