# marks1 = int(input("Enter marks 1"))
# marks2 = int(input("Enter marks 2"))
# marks3 = int(input("Enter marks 3"))
# marks4 = int(input("Enter marks 4"))
# marks5 = int(input("Enter marks 5"))

# total = marks1 + marks2 + marks3 +marks4 +marks5
# avg = total /5
# if avg >= 90:
#     print("Grade A")
# elif avg >= 75:
#     print("Grade B")
# elif avg >= 60:
#     print("Grade C")
# elif avg < 60 :
#     print("Grade D")
# n = int(input("Enter the number"))
#while loop 
# i = 1
# while i<=10:
#     print(f"{n} x {i} = {n*i}")
#     i+=1

# #for loop
# for i in  range(1,11):
#     print(f"{n} x {i} = {n*i}")

# while loop 
# i = 1
# while i <=10:
#     print(i)
#     i+=1

# #for loop
# for i in range(1,11):
#     print("i = ", i)

# 

# # Task 1
# subjects = ["maths" , "english" , "hindi", "science" , "social science"]
# for subject in subjects:
#     print(subject)

# # Task 2
# num1 = int((input("Enter the number 1"))) 
# num2 = int((input("Enter the number 2"))) 
# num3 = int((input("Enter the number 3"))) 
# num4 = int((input("Enter the number 4"))) 
# num5 = int((input("Enter the number 5"))) 


# nums = [num1 , num2 , num3 , num4 ,num5]
# sum = num1 + num2 + num3 + num4 +num5
# avg = sum/5
# if num1 > num2:
#     print


# # task 3 
# coordinates = ('x','y','z')
# print(coordinates[0] ,  "\n" , coordinates[1] , "\n" , coordinates[2] )


# numbers =   [10, 20, 30, 40, 50]
# numbers.append(60)
# numbers.insert(2,25)
# numbers.remove(30) 
# for number in numbers:
#     print(number)
# total = sum(numbers)
# avg = total/len(numbers)
# maximum = max(numbers)
# minimum = min(numbers)    
# print(f"number's total is {total}")    
# print(f"number's avg is {avg}")    
# print(f"number's maximum is {maximum}")    
# print(f"number's minimum is {minimum}") 
    

# #Task 1 
# name = input("Enter the name")
# print(len(name))
# print(name.upper())
# print(name.lower())
# print(name.isalpha())

# #Task2
# sen = input("Enter a sentence")
# print(sen.count("the"))
# print(sen.replace("the", "THE"))
# print(sen.split())

# #Task3
# full_name = "   sanu kumar   "
# full_name.strip()
# full_name.title()
# print(full_name)



# #Task 1 
# def greet_user(name):
#     print(f"hello , {name}!")
# greet_user("sanu")


# #Task2 
# def find_max(a,b,c):
#     print(f"The maximum num is {max(a,b,c)}")
# find_max(3,4,5)

# #Task3
# def calc_avg(num1 , num2 , num3 , num4 , num5):
#     avg = (num1 + num2 + num3 + num4 + num5)/5
#     if avg >= 90:
#         grade =  "A"
#     elif avg >= 75:
#         grade =  "B"
#     elif avg >= 60:
#         grade = "C"
#     else:
#         grade =  "D"

#     return avg , grade    
    
# avg , grade  = calc_avg(2 , 4 , 5, 7 , 8) 
# print(f"average : {avg} , grade = {grade}")  
    


# #Task1
# nums = [2, 3,4 ,5, 6]
# maxi = max(2,3,4,5,6)
# mini = min(2,3,4,5,6)
# total = 2+3+4+5+6
# avg = total/len(nums)
# print(maxi , mini , total , avg)

# #Task2
# coordinates = ('x','y','z')
# print(coordinates[0] ,  "\n" , coordinates[1] , "\n" , coordinates[2] )

# #Task3
# num = {1 , 2, 2 , 3, 4 , 3,1 }
# print(num)

# #Task4
# student = {
#     "Name" : "sanu kumar",
#     "Age" : 20,
#     "Marks" : 98,
#     "Grade" : "A"
# }
# print(student["Name"])
# print(student["Age"])
# print(student["Marks"])
# print(student["Grade"])

# student["Marks"] = 99
# print(student["Marks"])



# #Task1
# import numpy as np

# arr1 = np.array([10 , 20 , 30 , 40 ,50])

# print("sum:" , np.sum(arr1))
# print("mean" , np.mean(arr1))
# print("max" , np.max(arr1))
# print("min" , np.min(arr1))

# #Task2
# arr2 = np.array([[1,2,3] , [4,5,6]])
# print("shape" , arr2.shape)
# print(arr2[1,1])

# #Task3
# arr3 = np.array([2,3,4,6])
# print(arr3 * 3)
# lst = [2,3,4,6]
# print(lst * 3)


# import pandas as pd 

# #Task1
# data = pd.Series([2,3,4,5,6])
# print(data)
# print(data[3])

# #Task2
# data1 = {
#     "Name": ["Ram", "Shyam", "Geeta"],
#     "Age": [16, 17, 15],
#     "Subject": ["Math", "Science", "English"]
# }

# db = pd.DataFrame(data1)
# print(db)
# print(db["Subject"])

# #Task3
# print(db["Name"][1])
# print(db["Age"][2])




import pandas as pd 
df = pd.read_csv("student.csv")
print(df.head())
print(df.tail())
print(df.shape())
print(df.columns())
