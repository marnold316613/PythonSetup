# print('hello world')
# print('mike')    

# long_string = '''
# what up
# that's amazing
# see that

# '''

# print(long_string)

# # escape sequences
# weather ="\'98 degrees \"wow its hot\""
# # \t  = tab
# # \n  = new line
# print(weather)
# # formatted strings
# print(f'formatted string for weather: {weather}')
# # strings are just array
# print(weather[0:6:1])  # start and stop and step over
# print(weather[::2])
# print(weather[::-1])  # - means start from the end and work backwards
#                       # strings are immutable, you can't get do weather[0]='some value'
# print('length',len(weather))
# print(weather.upper())
from datetime import datetime


# birth_year=input('What year were you born?')

# mydate= datetime.today()

# print(mydate)

# print(datetime(int(birth_year),1,1))
# delta = mydate- datetime(int(birth_year),1,1)

# age = (int(delta.days/365.25))


# print(f"You are {age}")

# repeatcharacter='*'* 10  # this is an easy way to just repeat a character thru multiplication

# print('repeat chararcters', repeatcharacter)

# lists can be used like javascript arrays
li=[1,2,3,'a','b','c', True, False]
# list are mutable
li[3]='z'
# print(li)
# print(li[2])
# print(len(li))

# to copy a list use [:]  or .copy()
newLi=li[:]
newLi[3]='frank'
# print(li[::1])
# print(newLi[::1])
# matrix - a multidimensional array
matrix =[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
# print(matrix)
# print(matrix[0])
# print(matrix[1][1])

# matrix.append([100,200,300]) # adds to existing array, does not return a value
# print(matrix)

# matrix.insert(100,['a','b','c']) # insert modifies existing array, does not return a value
# print(matrix)

# matrix.extend([[3,4,5],[6,7,8]])
# print(matrix)

matrix.pop() # pops off whatever is at the end of the list and returns it
# matrix.pop(0) # pops off at index value and returns it

# matrix.remove([4,5,6])  # remove, removes a value from the array
# print(matrix)

# print(matrix.index(7)) # returns the index of the value, value must exist or an error is caused

# print('value' in matrix) # returns true false, # can also be used for searching strings

# print(matrix.count(3))  # returns how many times a value occurs in a list

# matrix.clear() # clears the list/array

# test= [1,2,3,4,5,11,'a','b','c','d','bb']  cannot sort arrays mixed of strings and int, at least not with default sorting

test= [1,2,3,4,5,11,12,6]

test=['a','b','bb','aa','ac','d']

test.sort() # sorts the existing array
print(test)
# sorted(matrix)  returns a new sorted array 

test.reverse()  # this reverses the index but does not sort the array

print(list(range(1,100)))  # creates an list with the values of 1 thru 99

' '.join  # is used to combine values into a single string, this returns a new string, whatever value is in ' ' becomes the separator, so usually a blank space

#list unpacking, mapping variables to values in a list, etc, works with tuples as well

a,b,c, *other = [1,2,3,4,5,6,7]  #*other assigns the rest of the array to its value

print(b)
print(other)

# None is a special value in python, probably like null
None 

# Dictionary  = an unordered key value pair, keys need to be unmutable, so basically only primitives
dictionary = {
  'a':1,
  'b':2
}
print(dictionary['a'])

user2=dict(name='fred', age=20)  # alternate way to create a dictionary
print(user2)
# .get will check if a key exists and returns None if it does not or the value if it has it
print(dictionary.get('a',22))  # an optional value can be added in case the key is not found

print('a' in dictionary.keys())

dictionary.update({'b':20})
dictionary.update({'c':30})  # if key doesn't exist its added


print(dictionary.items())

dictionary2=dictionary.copy()

# Tuple is an unmutable list
my_tuple=(1,2,3,4,5,6,6,6,6)

print(my_tuple)

# sets are unordered sets of unique objects

my_set = {1,2,3,4,5,5,5,12}
your_set= {4,5,6,7,8,9,10}
my_set.add(7)
my_set.add(1)
#print(my_set)
#print(set(my_tuple))
#print(list(my_tuple))
my_set.discard(5)

print(my_set.difference(your_set))  # difference returns a new set with diff
my_set.difference_update(your_set)  # updates the existing set

is_old= True
is_licensed=False
if is_old:
  print('condition met')  #indentation instead of brackets
elif is_licensed:
  print('help me')
else:
  print('whatever')

# truthy and falsy  0, '', None, etc are false
  # ternary operator
can_drive = "driving allowed" if is_old and is_licensed else "driving not allowed"
print('drive me',can_drive)

# went thru logical operators, they are the same as other languages

# == evaluates value not object type
# []==[] or 10 == 10.0
#  is is a reference comparison, the objects much share the same memory space, aka the same pointer
print('1' is '1')
print([] is [])  # false as they are different objects
# for loops 
for item in 'Zero to Mastery':
  print(item)

for item in my_set:
  print(item)

# iterables - list, dictionary, tuple, set, string
  
user= {
  'name': 'Golem',
  'age': 50,
  'can_swin': True
}

for item in user: # shows key only
  print(item)
for item in user.keys(): # shows key only
  print(item)

for item in user.items():  # gets key value pair
  print(item)

# for key,value in user: # another way to get key value
#   print(key, value)

for item in user.values():  # gets value
  print(item)

for item in (range(100)): #range starts at 0 by default and is counted as 1 so this range actually goes from 0 to 99
  print(item)

for _ in (range(0,100,2)):  #  _ is considered a disposable variable in python
  print(_)

for i,char in enumerate('Helloooo World'):  # enumerate just addes an index value to an iterable object
  print(i,char)

index=0
while index<50:
  index+=1
  print(index)
else:
  print('we are done') # else only works if there is no break in the while statement
