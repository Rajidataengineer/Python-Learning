# Python String Handling Management
#String = Sequence of character enclosed with ' ' or " "

#Assigning a string to the variable name

name = 'Rajeshwari'
print(name)
print(type(name))

#Get input from the user
user_name = input('Enter your name : ')
#Printing the user_name
print('Hello,',user_name,'!')
print("Hello," +user_name+ "!")

#print customized greeting using f-strings
print('Using f-string')
print(f'Hello,{user_name}!')

#String Operations
#Indexing / Slicing / Ranging

#Indexing---> Get a char from a string using its index value
#Positive Indexing--->indices start at 0 from the left
print(name)
print('Positive Indexing')
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
print(name[9])

#This process is called "Positive Indexing' and also called as Traversing

#Negative Indexing--->indices start at -1 from the right to access the character from the end
print('Negative Indexing')
print(name[-1]) #print last character in the name
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])
print(name[-8])
print(name[-9])
print(name[-10])



