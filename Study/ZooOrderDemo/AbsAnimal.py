#! /usr/bin/env python3
# MISSION: Supporting package for ''Python 2200: The Abc Module''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-2200
# DATE: 2023-08-09 13:09:32
# FILE: AbsAnimal.py
# AUTHOR: Randall Nagy
# The Random Zookeep
# Activity: Zoo Factory
#

import abc

class AbsAnimal(abc.ABC):
   def __init__(self, name='wild'):
      self.name = name
      self.health = 0
      
   @abc.abstractmethod
   def do_eat(self, food):
      pass
