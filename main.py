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

# to copy a list use [:]
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

matrix.remove([4,5,6])  # remove, removes a value from the array
print(matrix)

matrix.clear() # clears the list/array