class PlayerCharacter:
  #class object attribute, its a constant
  membership=True
  def __init__(self, name):
    self.name = name
  
  def run(self):
    print(f'run {self.name} the zombie is coming')

player1 = PlayerCharacter('mike')
player1.run()
