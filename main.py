print('hello world')
print('mike')    

long_string = '''
what up
that's amazing
see that

'''

print(long_string)

# escape sequences
weather ="\'98 degrees \"wow its hot\""
# \t  = tab
# \n  = new line
print(weather)
# formatted strings
print(f'formatted string for weather: {weather}')
# strings are just array
print(weather[0:6:1])  # start and stop and step over
print(weather[::2])
print(weather[::-1])  # - means start from the end and work backwards
                      # strings are immutable, you can't get do weather[0]='some value'
print('length',len(weather))
print(weather.upper())
