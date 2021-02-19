# Given the string:
s = 'flask'
# Use indexing to print out the following:
# 'f'

# 's'

# 'ask'

# 'las'

# 'k'

# Bonus: Use indexing to reverse the string

print(s[0])
print(s[3])
print(s[2:])
print(s[1:4])
print(s[-1])

rverse= s[::-1]
print(rverse)
print()

## Problem 2 ##
# Given this nested list:
mylist = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"

mylist[2][2] = "goodbye"
print(mylist)
print()

## Problem 3 ##
# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1["simple_key"])
print(d2["k1"]["k2"])
print(d3["k1"][0]["nest_key"][1][0])
print()
## Problem 4 ##
#Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
unique_values= set(mylist)
print(unique_values)
print(set(mylist))
print()

## Problem 5 ##
# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

print("Hello my dog's name is {0} and he is {1} years old".format(name, age))
print("Hello my dog's name is {Name} and he is {Age} years old".format(Age=age, Name=name))
sentence = "Hello my dog's name is {0} and he is {1} years old".format(name, age)
print(sentence)
