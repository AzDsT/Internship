#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1 - C
Question 2 - B
Question 3 - C
Question 4 - A
Question 5 - D
Question 6 - C
Question 7 - A
Question 8 - C
Question 9 - A B C
Question 10 - A B


# In[8]:


#Question 11
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input(" The factorial of this number : "))
print(factorial(n))


# In[9]:


#Question 12
Input=int(input("Enter a number to check prime or composite :"))
count=0
for number in range(1,Input+1):
    checknum = Input%number
    if checknum==0:
        count=count+1
        
if count == 2:
    print("This number is prime. ")
elif count>=3:
    print("This number is composite. ")


# In[12]:


#Question 13
string=input("Enter your string for check its Palindrome or not : ")
if string == string[::-1]:
    print("This is a Palindrome string")
else:
    print("This is not Palindrome string")


# In[14]:


#Question 14
def pythagoras (opposite_side, adjacent_side, hypotenuse):
    if opposite_side == str('x'):
        return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2)) ** 0.5))
    elif adjacent_side == str('x'):
        return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2)) ** 0.5))
    elif hypotenuse == str('x'):
        return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
    else:
        return "That is answer"

print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# In[17]:


#Question 15
input_string= "Data Science"
frequencies={}
for char in input_string :
    if char in frequencies:
        frequencies[char]+=1
    else:frequencies[char]=1
print("Per char frequency in '{}' is :\n {}".format(input_string, str(frequencies)))


# In[ ]:




