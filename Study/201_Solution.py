# MISSION: The complete set of examples and source code for ''Python 2200: The Abc
# Module''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-2200
# DATE: 2023-08-04 14:22:24
# FILE: 201_Solution.py
# AUTHOR: Randall Nagy
#
class Able:
	def do_name(self):
		self.name = input("Name: ")
		return self.name

class Baker(Able):
	def __init__(self, name):
		self.name = str(name)
	def get_name(self): return self.name
	def do_name(self): return super().do_name()

class Baker(Able):
	def __init__(self, name):
		self.name = str(name)
	def get_name(self): return self.name
	def do_name(self): return super().do_name()

a = Able()
b = Baker("Zillo")
isinstance(a, Able)
isinstance(a, Baker)
isinstance(b, Able)
isinstance(b, Baker)
