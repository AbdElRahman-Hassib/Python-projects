Exercise_Num=0
def Get_Exercise_Num():
    global Exercise_Num
    Exercise_Num=int(input("Enter the exercise number: "))

def special_multiplication(striing):
    new_string = ""
    for ind, s in enumerate(striing):
        new_string += s * (ind+1)
    return new_string

def max2(a,b):
    if a>b:
        return a
    return b

def max3(a,b,c):
    if c>b and c>a:
        return c
    return max2(a,b)

def max4(a,b,c,d):
    if d>c and d>b and d>a:
        return d
    return max3(a,b,c)

def max5(a,b,c,d,e):
    if e>d and e>c and e>b and e>a:
        return e
    return max4(a,b,c,d)

def max6(a,b,c,d,e,f):
    if f>e and f>d and f>c and f>b and f>a:
        return f
    return max5(a,b,c,d,e)

def Is_Prime(number):
    for i in range(2,number):
        if number%i==0:
            return False
    return True

def nth_Prime(n):
    number=0
    i=1
    while(number<n):
        i+=1
        while(Is_Prime(i)==False):
            i+=1
        number+=1
    return i

def nth_fibonacci(number):
    result=0
    last_result=0
    previous_last_result=1
    if number==1:
        return 0
    else:
        for i in range(2,number+1):
            result=last_result+previous_last_result
            previous_last_result=last_result
            last_result=result
        return result
    

Get_Exercise_Num()
if Exercise_Num==1:
    """This function takes a string and return nother string with each character repeated regarding it's index
    EX: abcd -> abbcccdddd"""
    print(special_multiplication("abcd"))
    print(special_multiplication("123456"))

elif Exercise_Num==2:
    """This functions return maximum number upon 2-6 numbers"""
    print(max2(2,8))
    print(max3(8,7,6))
    print(max4(8,7,6,5))
    print(max5(8,7,6,5,4))
    print(max6(8,7,6,5,4,3))

elif Exercise_Num==3:
    """This function is to get the Nth prime number"""
    print(nth_Prime(1))
    print(nth_Prime(2))
    print(nth_Prime(3))
    print(nth_Prime(4))
    print(nth_Prime(5))
    print(nth_Prime(6))
    print(nth_Prime(7))
    print(nth_Prime(8))
    print(nth_Prime(9))
    print(nth_Prime(10))

elif Exercise_Num==4:
    """This function is to get the Nth fibonacci number"""
    print(nth_fibonacci(1))
    print(nth_fibonacci(2))
    print(nth_fibonacci(3))
    print(nth_fibonacci(4))
    print(nth_fibonacci(5))
    print(nth_fibonacci(6))
    print(nth_fibonacci(7))
    print(nth_fibonacci(8))
    print(nth_fibonacci(9))
    print(nth_fibonacci(10))



