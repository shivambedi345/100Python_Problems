sideone=float(input("Enter the first side of the triangle: "))
sidetwo=float(input("Enter the second side of the triangle: "))
sidethree=float(input("Enter the third side of the triangle: "))
s=(sideone+sidetwo+sidethree)/2
area=(s*(s-sideone)*(s-sidetwo)*(s-sidethree))**0.5
print("Area of the triangle is: ",area)