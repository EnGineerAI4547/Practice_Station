#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # March 13th: Errors and Exceptions Homework

# ### Problem 1
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.

# In[14]:



for i in ['a','b','c']:
    while True:
        try: 
            print(i**2)

        except: 
            print(f"Sorry you can't raise the letter {i} to a power!")
            break


# ### Problem 2
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks. Then use a <code>finally</code> block to print 'All Done.'

# In[29]:


x = 5
y = 0


while True:
    
    try:
        z = x/y
        break
    except ZeroDivisionError:
        print("Error: division by zero ")
        y=int(input("Update the denominator: "))
    finally:
        z = x/y
        if y<=5:
            print("All done!")
            print(f"Z = {int(z)}")
            break
        else:
            print("All done!")
            print(f"Z = {z}")
            break
            
            
        


# ### ChatGPT optimized

# In[28]:


x = 5
y = 0

while True:
    
    try:
        z = x/y
        break
    except ZeroDivisionError:
        print("Error: division by zero ")
        y = int(input("Update the denominator: "))

if y <= 5:
    print("All done!")
    print(f"Z = {int(z)}")
else:
    print("All done!")
    print(f"Z = {z}")


# ### Problem 3
# Write a function that asks for an integer and prints the square of it. Use a <code>while</code> loop with a <code>try</code>, <code>except</code>, <code>else</code> block to account for incorrect inputs.

# In[5]:


def ask():
    while True:
        try:
            n=int(input("Please enter an integer: "))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            break
        
        
    print(f"The square of your number is {n**2}")
            


# In[6]:


ask()


# # Great Job!
