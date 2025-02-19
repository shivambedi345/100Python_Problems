def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
n=int(input("Enter a number: "))
if n<0:
    print("Enter a positive number")
elif n==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of",n,"is",fact(n))