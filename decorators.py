#decorators

import main  # import is how you get access to other python files
# a package is just files that are in a folder, you can then import foldername.filename
# all packages have a blank __init__.py file in them, it lets the interpreter know its a package

from time import time   # from allows you to just get a particular function

if __name__ == '__main__':   # this is how to test if the current file is the main file being run, 
  pass

def my_decorator(func):
  def wrap_func(*args, **kwargs):  # this pattern of *args, **kwargs keeps your decorator agnostic to the function it decorates
    print('*******')
    func(*args, **kwargs)
    print('*******')
  return wrap_func

@my_decorator
def hello(x,y,z):
  print(x,y,z)

hello('hello', ' how ', 'are you?')



def performance(func):
  def wrapper(*args, **kwargs):
    t1=time()
    result = func(*args,**kwargs)
    t2= time()
    print(f'it took {t2-t1} s')
    return result
  return wrapper

# @performance
# def long_time():
#   for i in range(10000000):
#     i*5

# long_time()

# error handling

# while True:
#   try:
#     age = int(input('what is your age? '))
#     print(age)
#   except ValueError:
#     print('you must enter a number only')
#   except ZeroDivisionError:
#     print('you must enter an age greater than 0')
#   except TypeError as err:
#     print(f'some other error occured {err}, please enter a number')
#   else:
#     print('thank you')
#     break
#   finally:
#     print('completed')
  
# generator functions, they work on demand
    
def generator_function(num):
  for i in range(num):
    yield i*2                            # yield seems to return after each iteration, it turns a function into a generator function

g = generator_function(100)

next(g)
next(g)
print(next(g))            #  next allows for the next iterator, so on this it is on its 3rd iteration
                          # if you call next more than the iteration, there will be a stopiteration error that will need to be trapped
def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      print(iterator)
      next(iterator)
    except StopIteration:
      break



