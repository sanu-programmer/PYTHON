a = int(input("Enter your age : "))

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering invalid age")

elif(a==0):
    print("Yor are entering 0 which is invalid age")    

else:
    print("You are below the age of consent")    