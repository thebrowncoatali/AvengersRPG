class Game():

	def _overview(self):
		'''
			Welcome and Overview about game
			Define a quest 
		'''
		print(
			'The Avengers RPG',
			'Welcome to the Avengers RPG game',
			'Hi. I\'m Nick Fury, Our mission is to protect the universe from',
			'the evil intentions of the titan Thanos.',
			'This mission will not be easy, you will undoubtedly face many challenges while on this mission',
			sep='\n'
		)

	def _ask_for_role(self):
		print(
			'=======================================================================',
			'All the avengers are busy and there are only left to fight this mission',
			'the egocentric and billionaire Tony Stark (IROMAN STATS: Strength: 2 Intelligence: 2 Agility: 1)',
			'and the young Peter Parker (Spiderman) (SPIDERMAN STATS: Strength: 1 Intelligence: -1 Agility: 2)',
			'Who do you want to be?',
			'=======================================================================',
			sep='\n'
		)

		character = None
		while not character:
			# Ask user choice
			character = input("(Enter 1 for Iroman or 2 for Spiderman): ")

			# Validate choice

			# First validation:
			try:
				character = int(character)
			except:
				print('\nInvalid choice, please try again. choice a number between [1-6]')
				character = None
				continue

			# Second Validation
			if character > 2 or character < 1:
				character = None

			# Error message
			if not character:
				print('\nInvalid choice, please try again. choice a number between [1-2]')

		if character == 1:
			print(
				'***You have chosen Iroman***',
				'Iroman: Is it better to be feared or respected?',
				sep='\n'
			)
		elif character == 2:
			print(
				'***You have chosen Spiderman***',
				'Spiderman: With Great Power, Comes Great Responsibility!',
				sep='\n'
			)


	def start(self):
		self._overview()
		self._ask_for_role()

