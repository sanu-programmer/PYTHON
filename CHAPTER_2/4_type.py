# Data Type
a = 31
t = type(a) # class <int>

print(t)

b = "31"
v = type (b) # class <str>
print(v)

c = 34.34
w = type(c) #class <float>
print(w)

# A number can be converted into a string and vice versa (if possible)
# There are many functions to convert one data type into another
d = int(b)
print(type(d)) #b but the type should be int


# Type conversion(Automatic conversion ) and Type casting(Manual conversion)
# Type conversion
a = 2
b = 4.25
sum = a + b # 2.00+ 4.25 = 6.25
print(sum)
# Type casting
a = int("2")
b = 4.25
print(a+b)

a = 3.14
a = str(a)
print(type(a))





