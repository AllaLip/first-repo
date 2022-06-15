import random
 
class Fighter:
  def __init__(self, name, health=100):
    self.name = name
    self.health = health
    print ('Fighter {}, health {}'.format(self.name, self.health))
 
  def strike(self, rivalFighter):
    if True:
      print('Fighter {} inflicted damage -20 to the fighter {}'.format(self.name, rivalFighter.name))
      rivalFighter.setHealth(rivalFighter.getHealth() - 20)
    else:
      print('Incorrectly set health for a fighter {}'.format(rivalFighter.name))
      print(type(rivalFighter.getHealth()))
 
  def setHealth(self, health):
    self.health = health
    print('Set health {} for fighter {}'.format(self.health, self.name))
 
  def getHealth(self):
    try:
      return self.health
      print("Fighter's health {} — {}".format(self.name, self.health))
    except:
      return 'Health is not set'
      print("For fighter {} health is not set".format(self.name))
 
 
 
f1 = Fighter('Ronda', 100)
f2 = Fighter('Miesha', 100)
 
while (f1.health > 0) and (f2.health > 0):
  round = random.randint(1, 2)
 
  if round == 1:
    f1.strike(f2)
  elif round == 2:
    f2.strike(f1)
 
if round == 1:
  name = f1.name
  rival = f2.name
elif round == 2:
  name = f2.name
  rival = f1.name
 
print('Fighter {} won the fight against {}'.format(name, rival))
