#!/usr/bin/env python
# coding: utf-8

# # Algorithm Workbench

# ### question 1 

# In[ ]:


# Write a while loop that lets the user enter a number. The number should be multiplied by 10, 
# and the result assigned to a variable named product. The loop should iterate as long as product is less than
Product = 0  

while Product < 100:
    user_input = float(input("Enter a number: "))
    Product = user_input * 10 

print(f"Result is {Product}, which is greater than or equal to 100.")


# In[49]:


# Write a while loop that lets the user enter a number. The number should be multiplied by 10, 
# and the result assigned to a variable named product. The loop should iterate as long as product is less than
Product = 0  

while Product < 100:
    user_input = float(input("Enter a number: "))
    Product = user_input * 10 

    print(f"Result is {Product}, which is greater than or equal to 100.")

    #the print statemnt was in the wrong indenation level needed to add tab to keep print statment in the loop 


# # question 2 

# In[2]:


# the question Write a while loop that asks the user to enter two numbers. The numbers should be added and the sum displayed
# The loop should ask the user if he or she wishes to perform the operation again.
# If so, the loop should repeat, otherwise it should terminate
answer = ('yes')
while answer == 'yes':
    num1 = float(input("enter the first number:"))
    num2 = float(input("enter the second number:"))
    num3 = num1 + num2
    print(f'sum is {num3}')
    answer = input("would you like to continue?")
# if yes the loop continue, anything else and the loop will stop 
# float input ask the user to enter 2 numbers for the function to complete 
# num3 3 is the printed statment that will be preformed after the num1 and num2 are answered 


# # question 1 - bug collector

# In[9]:


# question 1 is asking to calculate how much a bug collector collects bugs every day for five days. 
# Write a program that keeps a running total of the number of bugs collected during the five days
totalbugs = 0
for i in range(0,5):
    numbugs = float(input("enter the number of bugs collected:"))
    totalbugs += numbugs 
print(f'total bugs for the 5 day peirod {totalbugs}')
# set totalbugs = to 0 because starting point is 0 
# for i in range function is to run the function 0,1,2,3,4 which equals up to 5 times 
# totalbugs += numbugs is to add the numbugs each time the function is run


# # question 4 - distance traveled 

# In[10]:


# Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled.
# It should then use a loop to display the distance the vehicle has traveled for each hour of that time period.
speed = float(input('enetr the speed in mph'))
t0tal_hour = float(input('enetr the hours traveled'))
for hour in range (1,total_hour + 1):
    distance = speed * hour
    print(f'{hour}          {distance}')
# ask user to put input in for speed and toatal hours for the function to run
# for hour in range is setting the pattern or equation for the users input givin and spitting out the distance
# equation will give the distances and hours for the function and give correct answer 


# In[11]:


speed = float(input('enetr the speed in mph'))
total_hour = float(input('enetr the hours traveled'))
for hour in range (1,total_hour + 1):
    distance = speed * hour
    print(f'{hour}          {distance}')
# total_hours line was misspelled            


# In[14]:


speed = float(input('enetr the speed in mph'))
total_hour = int(input('enetr the hours traveled'))
for hour in range (1,total_hour + 1):
    distance = speed * hour
    print(f'{hour}          {distance}')
# () were missplaced not closed off correctly           


# #  number 13 - draw pattern 

# In[17]:


#  Write a program that uses nested loops to draw this pattern:
for I in range(7,0,-1):
    for j in range(0,I):
        print('*')
# for I in range is starting at 7 * per line and removing one each line after so , 7,6,5,4,3,2,1
# for j in range(0,I) nested loop we created in new function 
# print * per line 


# In[29]:


for I in range(7,0,-1):
    for j in range(0,I):
        print('*', end='')
    print('\n')
    
# I = 7
# j = 0
# *
# j = 1
# *
# j = 2 3 4 5 6
# \n
# I = 6
# j = 0
# ******
# \n
# I = 5
# example of how the code runs down line to line 
# first attemped needed to add end='') and  print('\n') for * to indent in correct spot 
# else code will only have correct amount of * and wrong identation 


# In[40]:


for I in range(7,0,-1):
    for j in range(0,I):
        print('*',end='')
    print('') 
# ('\n') was unnecessary added indent between pattern created spaces between the printed function 


# # number 14 - draw pattern 

# In[41]:


# Write a program that uses nested loops to draw this pattern:
for I in range(0,6):
    for J in range(0,I):
        print(' ',end='')
    print('#')
# the I and J are nested loop for the equation 
# 6 lines down is the amount if lines that need to be filled 


# In[42]:


for I in range(0,6):
    for J in range(0,I):
        print('# ',end='')
    print('#')
# added another # in print statment to copy pattern 


# In[43]:


for I in range(0,6):
    print('#')
    for J in range(0,I):
        print(' ',end='')
    print('#')
# indentation is in the wrong spot 
# confused code by adding double # in the nested loop need to start next row of # before nested loop starts 


# In[44]:


for I in range(0,6):
    print('#',end='')
    for J in range(0,I):
        print('#',end='')
    print(' ')
# added end='') to statment to move back start of function indenting
# indentation is correct and print end function are working 


# In[ ]:




