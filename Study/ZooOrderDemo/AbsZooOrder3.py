#! /usr/bin/env python3
# MISSION: Supporting package for ''Python 2200: The Abc Module''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-2200
# DATE: 2023-08-09 18:30:56
# FILE: AbsZooOrder3.py
# AUTHOR: Randall Nagy
# The Random Zookeep
# Activity: Testable Zoo Factory
#
import abc
import random
from ZooFood import Food
import ConBird, ConCat, ConBear


class GameParams:

   def __init__(self, title):
      self.title = title
      self.zoo = []

   @abc.abstractmethod
   def create_zoo(self):pass

   @abc.abstractmethod
   def get_food(self):pass

   @staticmethod
   @abc.abstractmethod
   def mk_game():pass

   @staticmethod
   def mk_game(is_test):
      if is_test:
         return TestableGameParams.mk_game()
      else:
         return ClassicGameParams.mk_game()



class TestableGameParams(GameParams):

   def __init__(self, title):
      super().__init__(title)

   def create_zoo(self):
      return self.zoo

   def get_food(self):
      return Food.BIRD_FOOD

   #@staticmethod
   def mk_game():
      results = TestableGameParams("Testable Game!")
      results.zoo = []
      for which in range(1,11):
         if which % 2 == 0:
            results.zoo.append(ConBird.Bird())
         elif which % 3 == 0:
            results.zoo.append(ConCat.Cat())
         else:
            results.zoo.append(ConBear.Bear())
      return results


class ClassicGameParams(GameParams):
   
   def __init__(self, title='Classic Game!'):
      super().__init__(title)

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

   #@staticmethod
   def mk_game():
      results = ClassicGameParams("Classic Game!")
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

