#!/usr/bin/env python
# coding: utf-8

# # List Comprehension

# #### 1. Basic Syntax  list =[expression for item in iterable]

# In[1]:


numbers = [x for x in range(1,6)]
print(numbers)


# #### 2.With Expression(Math Operation)

# In[4]:


squares = [x**2 for x in range(1,6)]
cubes = [x**3 for x in range(1,6)]
print(squares)
print(cubes)


# #### 3.With Condition(IF Filter)

# In[5]:


evens = [x for x in range(1,11) if x % 2 == 0]
odds = [x for x in range(1,11) if x % 2 != 0]
print(evens)
print(odds)


# #### 4.IF-ELSE Inside Comprehension

# In[8]:


result = ['Even' if x % 2 == 0 else 'Odd' for x in range(1,6)]
print(result)


# #### 5. With String

# In[9]:


words = ['apple','grapes','lemon']
upper = [w.upper() for w in words]
print(upper)


# #### 6.List Comprehension vs For Loop

# In[14]:


# Traditional Loop
result = []
for x in range(1,6):
   result.append(x*2)
print(result)

#List Comprehension
result = [x*2 for x in range(1,6)]
print(result)


# #### 7. Nested List Comprehension(Multiplication Table)

# In[15]:


table = [[i * j for j in range(1,4)] for i in range(1,4)]
for row in table:
    print(row)

