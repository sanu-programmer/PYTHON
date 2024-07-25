# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

marks1 = int(input("Enter the marks of sub 1: "))
marks2 = int(input("Enter the marks of sub 2: "))
marks3 = int(input("Enter the marks of sub 3: "))


total_percentage = ((marks1+ marks2+ marks3)/300)*100

if(total_percentage>40 , marks1>=33 , marks2>=33 , marks3>=33):
    print("your percentage is " ,total_percentage ," Congratulation! You are Pass",)

else:
    print("your percentage is " ,total_percentage ,"You failed , try again next year", )    


