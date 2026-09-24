#! /usr/bin/env python3
# MISSION: Supporting package for ''Python 2200: The Abc Module''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-2200
# DATE: 2023-08-09 16:18:08
# FILE: ZooOrder2.py
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
   def create_zoo(self):
      return self.zoo

   @abc.abstractmethod
   def get_food(self):
      return Food.BIRD_FOOD

   @staticmethod
   def mk_game():
      results = GameParams("Testable Game!")
      results.zoo = []
      for which in range(1,11):
         if which % 2 == 0:
            results.zoo.append(ConBird.Bird())
         elif which % 3 == 0:
            results.zoo.append(ConCat.Cat())
         else:
            results.zoo.append(ConBear.Bear())
      return results
