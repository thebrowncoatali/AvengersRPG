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

	def start(self):
		self._overview()

