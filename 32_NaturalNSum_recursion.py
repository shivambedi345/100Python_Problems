def naturalnumsum(n):
    if n == 1:
        return 1
    else:
        return n + naturalnumsum(n-1)
n=int(input("Enter a number: "))
if n<0:
    print("Enter a positive number")
else:
    print("The sum of first",n,"natural numbers is",naturalnumsum(n))