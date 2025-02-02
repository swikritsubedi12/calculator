def addnumbers():
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    sum=a+b
    return sum
def subnumbers():
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    sub=a-b
    return sub
def multiply():
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    multiply=a*b
    return multiply
def divide():
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    divide=a/b
    return divide
while True:
    print("""Enter your choice
        1. Addition
        2. Substraction
        3. Multiply
        4. Divide
        5. Exit""")
    choice=int(input("Enter your choice: "))
    if choice==1:
        result=addnumbers()
        print("The sum is: ",result)
    elif choice==2:
        result=subnumbers()
        print("The difference is: ",result)
    elif choice==3:
        result=multiply()
        print("The product is: ",result)
    elif choice==4:
        result=divide()
        print("The remaining number is: ",result)
    else:
        print("Exit!!")
        break