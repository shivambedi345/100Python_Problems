print("Numbers divisible by 13 in the range of 1 to 100 are:")
for i in range(1,100):
    if i % 13 == 0:
        print(i)
        
# using lambda function and filter function
l= list(filter(lambda x: x % 13 == 0, range(1,100)))
print("Numbers divisible by 13 in the range of 1 to 100 are:", l)     
        