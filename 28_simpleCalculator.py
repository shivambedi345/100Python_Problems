num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
opr=input("""Enter the operatorion you want to perform:
    1.addition
    2.subtraction
    3.multiplication
    4.division
    5.modulus   
    6.exponentiation
    """)
if opr=='1':
    print("The sum of",num1,"and",num2,"is",num1+num2)
elif opr=='2':
    print("The difference of",num1,"and",num2,"is",num1-num2)
elif opr=='3':
    print("The product of",num1,"and",num2,"is",num1*num2)
elif opr=='4':
    print("The division of",num1,"and",num2,"is",num1/num2)
elif opr=='5':
    print("The modulus of",num1,"and",num2,"is",num1%num2)
elif opr=='6':
    print("The exponentiation of",num1,"and",num2,"is",num1**num2)
else:
    print("Invalid input")