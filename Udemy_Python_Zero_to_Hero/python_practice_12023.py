#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Object Oriented Programming Challenge
# 
# For this challenge, create a bank account class that has two attributes:
# 
# * owner
# * balance
# 
# and two methods:
# 
# * deposit
# * withdraw
# 
# As an added requirement, withdrawals may not exceed the available balance.
# 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

# In[42]:


class Account:
    
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        
        
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
    
    def deposit(self,dep_amt):
        self.balance+=dep_amt
        print("Deposit Accepted")
        
    def withdraw(self, with_amt):
        if (with_amt<=self.balance):
            self.balance-=with_amt
            print(f"New balance: ${self.balance}")
        else:
            print("Insufficient Funds!")
    


# In[43]:


# 1. Instantiate the class
acct1 = Account('Jose',100)


# In[44]:


# 2. Print the object
print(acct1)


# In[45]:


# 3. Show the account owner attribute
acct1.owner


# In[46]:


# 4. Show the account balance attribute
acct1.balance


# In[47]:


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)


# In[48]:


acct1.withdraw(75)


# In[49]:


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


# ## Good job!
