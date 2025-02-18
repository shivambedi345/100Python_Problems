import cmath
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
c = input("Enter the value of c: ")
d = b**2-4*a*c
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print("The solutions are {0} and {1}".format(sol1,sol2))

    
