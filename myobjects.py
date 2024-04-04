class PlayerCharacter:  # we Pascal case as a convention so others know this is a class
  #class object attribute, its a constant
  membership=True
  def __init__(self, name):
    self.name = name
  
  def run(self):
    print(f'run {self.name} the zombie is coming')
  @classmethod
  def adding_things(cls,num1,num2):  # this is a static method, cls is like self, it refers back to the class, this is by convention not by name
    return num1+num2
  @staticmethod   # a true static method, it has no reference to the class object
  def addint_thingstatic(num1,num2):
    return num1+num2

player1 = PlayerCharacter('mike')
player1.run()

# there are no truly private variables in python, _variablename is way to let others know the _ means private

class User():
  def __init__(self,email):
    self.email=email
  def sign_in(self):
    print('logged in')

class Wizard(User):
  def __init__(self, email):
    super().__init__(email)
    print(self.email)

class Archer(User):
  pass

wizard1 = Wizard("mike@email.com")
wizard1.sign_in()

#print(isinstance(wizard1,User))

# in multiple inheritance scenarios which is something i avoid but python allows
# there is something called mro()  which is method resolution order, a way to resolve methods when there is multiple inheritance
