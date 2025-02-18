num = int(input("Enter a positive number: "))

if num < 0:
    print("Enter a positive number")
else:
    total_sum = 0
    i = 1  # Start from 1

    while i <= num:
        total_sum += i
        i += 1  # Increment counter

    print("The sum is", total_sum)



    