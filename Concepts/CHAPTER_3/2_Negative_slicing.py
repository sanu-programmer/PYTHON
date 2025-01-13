name = "Sanu kumar"

print(name[0:3])


print(name[-4:-1])
print(name[6:9])

print(name[:4]) # Starting position blanks means starting from 0.
print(name[1:]) #Last position blank means going to last position.
print(name[1:10]) #is same as [1:]


# We can provide a skip value as a part of our slice like this:
word = "amazing"
print(word[1:6]) #mazin
print(word[1: 6: 2]) # "mzn

