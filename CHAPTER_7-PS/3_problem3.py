# Write a program to print multiplication table of a given number using while loop. 

t = int(input("Enter the table: "))

i = 1
while(i<=10):
    print(f"{t} x {i} = {t*i}")
    i+=1