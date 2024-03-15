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

print(li)
print(li[2])
print(len(li))
