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
