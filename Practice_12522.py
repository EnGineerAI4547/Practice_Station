#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In the today's lecture we begin practicing the basic components that will be used to create our tic tac toe game bb


# In[1]:


# start by representing a list 

list1=[1,2,3]

print(list1)


# In[2]:


# Next we create 3 lists stacked 

print(list1)
print(list1)
print(list1)


# In[11]:


#now we replace the numbers in the list to create an empty list format that can graphically represent a tic tac toe board
# we will also create a function that can be used to call the lists instead of typing them seperately 

#this function will take three input lists and output them to create a tic tac toe board
def list_print(list1,list2,list3):
    print(list1)
    print(list2)
    print(list3)

    


# In[51]:


list1=[" "," "," "]
list2=[" "," "," "]
list3=[" "," "," "]


# In[42]:


list2[1]="x"
list_print(list1,list2,list3)


# In[ ]:


# Next we practice inputting variables with user input 


# In[52]:


# so next we will ask user for input and store it in a variable. We have to staty mindful of the fact that python casts input 
# as a string by default so we will have to use the built in castable functions to convert our input when needed
list4=[" 1"," 2"," 3"]
list5=[" 4"," 5"," 6"]
list6=[" 7"," 8"," 9"]


print("Hey user please give me an index you wish to place your 'X':")
print("You may choose a number but do not write it out! Input an integer.")
print("For example:\n")

list_print(list4,list5,list6)


# In[53]:


int_choice1=int(input("Please choose your number:"))


# In[54]:


if int_choice1 <=3:
    list1[int_choice1]="X"
if ((int_choice1 >=3) and (int_choice1 <=6)):
    list2[int_choice1-4]="X"
if ((int_choice1 >=3) and (int_choice1 >=6) and (int_choice1 <=9)):
    list3[int_choice1-7]="X"
    
list_print(list1,list2,list3)


# In[ ]:


#***This concludes the practice for today. Tomorrow's python practice will feature exceptions and input checking****

