# MISSION: The complete set of examples and source code for ''Python 2200: The Abc
# Module''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-2200
# DATE: 2023-08-12 10:23:58
# FILE: 501_Solution_Suprize.py
# AUTHOR: Randall Nagy
#
import abc

class Able(abc.ABC):
   def __init__(self): self._name = ''      
   def do_name(self):
      self._name = input("Name: ");return self._name   

   @property
   @abc.abstractmethod
   def name(self): return self._name   

   @name.setter
   @abc.abstractmethod
   def name(self, a_value): ...      

   @name.deleter
   @abc.abstractmethod
   def name(self): self._name = ''


class Baker(Able):

   @property
   def name(self):
      return super().name

   @name.setter # regression?
   def name(self, a_value):
      self._name = str(a_value)
      
   @name.deleter # regression?
   def name(self):
      self._name = 'deleted'


