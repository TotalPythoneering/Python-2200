#! /usr/bin/env python3
# MISSION: Supporting package for ''Python 2200: The Abc Module''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-2200
# DATE: 2023-08-09 13:33:45
# FILE: ConBear.py
# AUTHOR: Randall Nagy
# The Random Zookeep
# Activity: Zoo Factory
#
from ZooFood import Food
from ConCat import Cat

class Bear(Cat):
   def __init__(self):
      super().__init__("Bear")
      
   def do_eat(self, food):
      if isinstance(food, Food):
         if food is Food.BEAR_FOOD:
            self.health += 5
            return True
      return False
