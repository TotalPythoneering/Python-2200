#! /usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 2200: The Abc
# Module''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-2200
# DATE: 2023-08-09 11:43:49
# FILE: sol_AnimalHouseBear.py
# AUTHOR: Randall Nagy
# The Random Zookeep
# Activity: Bears eat cat food ...
#
import enum

class Food(enum.Enum):
   BIRD_FOOD = 1
   CAT_FOOD  = 2
   BEAR_FOOD = 3 # New!

import abc

class AbsAnimal(abc.ABC):
   def __init__(self, name='wild'):
      self.name = name
      self.health = 0
      
   @abc.abstractmethod
   def do_eat(self, food):
      pass

class Bird(AbsAnimal):
   def __init__(self):
      super().__init__("Bird")
      
   def do_eat(self, food):
      if isinstance(food, Food):
         if food is Food.BIRD_FOOD:
            self.health += 5
            return True
      return False

class Cat(AbsAnimal):
   def __init__(self, name='Cat'): # New!
      super().__init__(name)
      
   def do_eat(self, food):
      if isinstance(food, Food):
         if food is Food.CAT_FOOD:
            self.health += 5
            return True
      return False


class Bear(Cat):  # New!
   def __init__(self):
      super().__init__("Bear")
      
   def do_eat(self, food):
      if super().do_eat(food) is False:  # New!
         if food is Food.BEAR_FOOD:
            self.health += 5
            return True
      return False


import random
zoo = []
for _ in range(10):
   which = random.randrange(3)
   if which == 0:
      zoo.append(Bird())
   elif which == 1:
      zoo.append(Cat())
   elif which == 2:
      zoo.append(Bear())
   else:
      raise Exception("Random range problem.")

print(*zoo, sep='\n')

if not issubclass(Bear, Cat):
   raise Exception("Crazy Bear")
if not issubclass(Cat, AbsAnimal):
   raise Exception("Crazy Cat")
if not issubclass(Bird, AbsAnimal):
   raise Exception("Crazy Bird")   
if issubclass(Bird, Cat):
   raise Exception("Unloved Bird")   
if issubclass(Cat, Bird):
   raise Exception("Unloved Cat")   
if issubclass(Bear, Bird):
   raise Exception("Unloved Bear")   

done = False
while not done:
   for pet in zoo:
      which_food = random.randrange(1,4)
      if which_food == 1:
         pet.do_eat(Food.BIRD_FOOD)
      elif which_food == 2:
         pet.do_eat(Food.CAT_FOOD)
      elif which_food == 3:
         pet.do_eat(Food.BEAR_FOOD)
      else:
         raise Exception(f'Unable to feed {pet.name}')
      
      if pet.health > 20:
         print(pet.name, "wins!")
         done = True
         break

