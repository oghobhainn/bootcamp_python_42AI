import sys

class GotCharacter:
	"""Class building a GoT character (thanks captain obvious)
	
		-first_name
		-is_alive (default is True)

	"""

	def __init__(self, first_name, is_alive = True):

		self.first_name = first_name
		self.is_alive = is_alive

class Stark(GotCharacter):
	"""A class representing the Stark family. Or when bad things happen to good people.

		-family_name
		-house_words

	"""

	def __init__(self, first_name=None, is_alive=True):

		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

	def print_house_words(self):
		print(self.house_words)
	
	def die(self):
		if self.is_alive == True:
			print("The character dies !")
			self.is_alive = False
		else:
			print("The character is already dead !")

