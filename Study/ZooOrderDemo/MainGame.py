#! /usr/bin/env python3
# MISSION: Supporting package for ''Python 2200: The Abc Module''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-2200
# DATE: 2023-08-10 12:57:19
# FILE: MainGame.py
# AUTHOR: Randall Nagy
# The Random Zookeep
# Activity: Zoo Factory
#
from AbsZooOrder3 import GameParams

my_game = GameParams.mk_game(False) # New!

import random
zoo = my_game.create_zoo() # New!

print(*zoo, sep='\n')

done = False
while not done:
   for pet in zoo:
      which_food = my_game.get_food() # New!
      pet.do_eat(which_food)      
      if pet.health > 20:
         print(pet.name, "wins!")
         done = True
         break

