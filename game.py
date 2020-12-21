import die_roll 
from roles import spiderman

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

	def _rules(self):
		print(
			'======================================================================================================',
			'Along your journey you will come across 3 challenges.',
			'In order to win the game you must win all 3 challenges.',
			'You may lose the game if you lose at least two challenges or the last challenge',
			'When you come across these challenges, you will be required to roll two 6 sided die by typing "roll"',
			'You may win or lose the challenge depending on the roll you got and the stats of your chosen character',
			'Rolling a 2-4 is a critical loss, and associated stats are decreased',
			'Rolling a 5-7 is a loss, associated stats remain the same',
			'Rolling a 8-11 is a win, associated stats remain the same',
			'Rolling a 12 is a critical win, associated stats increase.',
			'======================================================================================================',
			sep='\n'
		)

	def _ask_for_role(self):
		print(
			'======================================================================================================',
			'All the avengers are busy and there are only left to fight this mission',
			'the egocentric and billionaire Tony Stark (IROMAN STATS: Strength: 2 Intelligence: 2 Agility: 1)',
			'and the young Peter Parker (Spiderman) (SPIDERMAN STATS: Strength: 1 Intelligence: -2 Agility: 2)',
			'Who do you want to be?',
			'======================================================================================================',
			sep='\n'
		)

		character = None
		while not character:
			# Ask user choice
			character = input("(Enter 1 for Spiderman or 2 for Iroman): ")

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
				'***You have chosen Spiderman***',
				'Spiderman: With Great Power, Comes Great Responsibility!',
				'\n',
				sep='\n'
			)
			role = spiderman.Spiderman(1,-2,2)
		elif character == 2:
			print(
				'***You have chosen Iroman***',
				'Iroman: Is it better to be feared or respected?',
				'\n',
				sep='\n'
			)

		count = 0
		special = 0

		if character == 1:
			# Challenge #1
			print('The infinity gauntlet is in the hands of the chitauris and \nthey are about to take it to Thanos. You need to use your Strength (STR) to follow them and remove it.\n***In order to be successful in this challenge you need to roll higher than a 6***')

			roll = die_roll.DiceRoll(input("Enter 'roll': "))
			print('you rolled ' + str(roll))
			STR = role[0]
			bonus = roll + STR
			print('you rolled ' + str(bonus) + ' with stat bonuses')

			roll_state = die_roll.RollStatements(bonus)
			stat_str = spiderman.Strength(bonus, STR)

			print(roll_state + "\nyou now have " + str(stat_str) + " STR")

			#loss counter
			if (bonus <= 5):
				count += 1
			#special ending
			if(bonus >= 12):
				special +=1

			# Challenge #2
			print('You have managed to remove the gauntlet from the chitauris, you give it to the black panther\n, now you must face the villain Ebony Maw who is fighting to keep the gauntlet of infinity.You need to fast to dodge their attacks (AGL).\n***In order to be successful in this challenge you need to roll higher than a 6***')

			roll = die_roll.DiceRoll(input("Enter 'roll': "))
			print('you rolled ' + str(roll))
			AGL = role[2]
			bonus = roll + AGL
			print('you rolled ' + str(bonus) + ' with stat bonuses')

			roll_state = die_roll.RollStatements(bonus)
			stat_agl = spiderman.Agility(bonus, AGL)

			print(roll_state + "\nyou now have " + str(stat_agl) + " AGL")

			#loss counter
			if (bonus <= 5):
				count += 1
			#special ending
			if(bonus >= 12):
				special +=1

			#Game over detection
			if count == 2:
				print(spiderman.WinLossStatements(count,special))
				exit()

			# Challenge #3
			print('You have defeated Ebony Maw, the panther is in trouble and the gauntlet is rolling on the ground, you must invent a good movement (INT) to catch it and throw it at Iroman.\n***In order to be successful in this challenge you need to roll higher than a 6***')

			roll = die_roll.DiceRoll(input("Enter 'roll': "))
			print('you rolled ' + str(roll))
			INT = role[1]
			bonus = roll + INT
			print('you rolled ' + str(bonus) + ' with stat bonuses')

			roll_state = die_roll.RollStatements(bonus)
			stat_int = spiderman.Intelligence(bonus, INT)

			print(roll_state + "\nyou now have " + str(stat_int) + " INT")
	
			#loss counter
			if (bonus <= 5):
				count += 2
			#win game => spiderman
			#game over => spiderman

			print(spiderman.WinLossStatements(count,special))#spiderman win and loss statements 
		


	def start(self):
		self._overview()
		self._rules()
		self._ask_for_role()

