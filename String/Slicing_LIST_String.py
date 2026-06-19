# Slicing --> getting a particular portion of a string using :
# Slicing Syntax--> Sequence[Start:Stop:step]

# How Slicing works in LIST

numbers = [0,1,2,3,4,5,6,7,8,9]
# Basic Slicing (Extract indices 2 to 4)
print(numbers[2:5])
# Omitting Start (Slice from beginning upto index 3)
print(numbers[:4])
# Omitting Stop (Slice from index 5 to the very end)
print(numbers[5:])
# Using  Steps (Extract every second element from index 1 to 7)
print(numbers[1:8:2])

#How Slicing works in String

word = 'Environment'
print(word[0:5]) # To Print 'ENVIR'
print(word[0:12:2])
print(word[-3:]) #To get last 3 character using negative index
print(word[::-1]) # Tp reverse a string
