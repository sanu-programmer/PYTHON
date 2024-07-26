# Write a program to find whether a given number is prime or not.

p = int(input("Enter the number: "))
for i in range(2 ,p):
        if(p%i == 0):
            print("It is not a prime number")
            break
else:
    print("It is a prime number")            