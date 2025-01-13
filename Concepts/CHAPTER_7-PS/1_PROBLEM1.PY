# Write a program to print multiplication table of a given number using for loop. 

t = int(input("Enter the table:"))
for i in range(1,11):
    # print(t,"x",i,"=",i*t) # This is one method instead of it we can also use f string
    print(f"{t} x {i} = {t*i}")