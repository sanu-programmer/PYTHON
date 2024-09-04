'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2x1
factorial(3) = 3x2x1
factorial(4) = 4x3x2x1
factorial(n) = nx(n-1) X (n-2) X..........3X2X1
FACTORIAL(n) = n X factorial(n-1)

'''
def factorial(n):
    if(n==0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
    

n = int(input("Enter the number: "))
print(f"The factorial of this number is: {factorial(n)}")    


