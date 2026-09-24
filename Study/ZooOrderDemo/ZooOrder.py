#! /usr/bin/env python3
# MISSION: Supporting package for ''Python 2200: The Abc Module''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-2200
# DATE: 2023-08-09 13:57:13
# FILE: ZooOrder.py
# AUTHOR: Randall Nagy
# The Random Zookeep
# Activity: Zoo Factory
#

import random
from ZooFood import Food
import ConBird, ConCat, ConBear

class GameParams:

   def __init__(self, title):
      self.title = title
      self.zoo = []

   def create_zoo(self):
      return self.zoo

   def get_food(self):
      which_food = random.randrange(1,4)
      if which_food == 1:
         return Food.BIRD_FOOD
      elif which_food == 2:
         return Food.CAT_FOOD
      elif which_food == 3:
         return Food.BEAR_FOOD
      else:
         raise Exception(f'Unable to feed {pet.name}')

   @staticmethod
   def mk_game():
      results = GameParams("Classic Game!")
      results.zoo = []
      for _ in range(10):
         which = random.randrange(3)
         if which == 0:
            results.zoo.append(ConBird.Bird())
         elif which == 1:
            results.zoo.append(ConCat.Cat())
         elif which == 2:
            results.zoo.append(ConBear.Bear())
         else:
            raise Exception("Random range problem.")
      return results
