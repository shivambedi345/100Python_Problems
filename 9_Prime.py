num = int(input("Enter a number: "))  # Use int instead of float for proper looping

if num < 2:
    print("Enter a number greater than 1")
else:
    for i in range(2, int(num**0.5) + 1):  # Optimize: Check only up to √num
        if num % i == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")
