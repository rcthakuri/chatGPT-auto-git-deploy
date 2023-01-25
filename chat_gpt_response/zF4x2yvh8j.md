

// Program to find the factorial of a number in Python

# Function to calculate the factorial of a number
def factorial(n):
    # Initializing the factorial variable to 1
    fact = 1
    # Looping over the number and calculating the factorial
    for i in range(1, n+1):
        fact *= i
    # Returning the factorial of the number
    return fact

# Taking the input from the user
num = int(input("Enter a number: "))

# Calling the function and printing the result
print("The factorial of", num, "is", factorial(num))