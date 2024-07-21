num1, operation, num2 = input("""Enter your mathematical expression""").split()
print(type(num1),type(operation))

if operation == "+":
    print(int(num1)+int(num2))
elif operation == "-":
     print(int(num1)-int(num2))
elif operation == "*":
     print(int(num1)*int(num2))
elif operation == "/":
    print(int(num1)/int(num2))

