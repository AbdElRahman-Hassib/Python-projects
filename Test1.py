"""
first_num,second_num=map(float,input("enter two numbers:").split())
print(type(first_num))
print((second_num))
print(str(first_num)+"+"+str(second_num)+"=",first_num+second_num)
print(str(first_num)+"-"+str(second_num)+"=",first_num-second_num)
print(str(first_num)+"*"+str(second_num)+"=",first_num*second_num)
print(str(first_num)+"/"+str(second_num)+"=",first_num/second_num)
"""
a,b,c=map(int,input("enter three numbers:").split())

temp=a
a=b
b=c
c=temp

print(a,b,c)