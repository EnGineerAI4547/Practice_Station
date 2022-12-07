#!/usr/bin/env python
# coding: utf-8

# # Practice 12/7/22: Practicing Python Input Verification
# ### For today's practice we are fleshing out one building block, user input,of what will eventually be a python tic tac toc game
# 

# ## Define a function to take user input :

# In[3]:


#ion the function we dont need to take any input as parameters. Only give output 
def user_input():
    # we'll need values to keep the loop going until two conditions are met:
    # 1.) user input is verified as an int and 2.) user input is in an acceptable range
    
    #flag variable 
    choice="false"
    range_check=False
    acceptable_range=range(1,9)
    
    
        
    
    while choice.isdigit()==False or range_check==False:
        choice=input("Please select a position from (1-9):")
        
        
        if choice.isdigit()==False:
            print("Sorry, incorrect input format! Please try again.")
        
        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                range_check=True
            else:
                print("Sorry the number you chose is not in the accepted range! ")
                print("Please try again!")
                pass
    
            
    return int(choice)    
        


# # Function call 

# In[4]:


user_input()

