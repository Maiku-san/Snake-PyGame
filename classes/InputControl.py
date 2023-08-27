import pygame

class InputControl:
	
	def __init__(self, game, player1):
		self.game = game
		self.player1 = player1


	def handle_input(self):
		# handle buttons
		if self.game.quit_button.clicked is True:
			self.game.check_high_score()

			self.game.is_on = False

		if self.game.play_button.clicked is True:
			self.game.is_paused = False
			self.game.active_screen = 'game screen'
			for i in range(len(self.game.menu_buttons)):
				self.game.menu_buttons[i].clicked = False

		# handle events
		for event in pygame.event.get():
			# check if the user clicked x at the top right corner to close the game
			if event.type == pygame.QUIT:
				self.game.check_high_score()
				
				self.game.is_on = False

			# handle keyboard controls
			if event.type == pygame.KEYDOWN:
				if self.game.is_paused is False:
					if event.key == pygame.K_UP:
						self.player1.change_direction_to = 'UP'
					if event.key == pygame.K_DOWN:
						self.player1.change_direction_to = 'DOWN'
					if event.key == pygame.K_LEFT:
						self.player1.change_direction_to = 'LEFT'
					if event.key == pygame.K_RIGHT:
						self.player1.change_direction_to = 'RIGHT'

				# press ESC to bring up menu screen and pause the game
				if event.key == pygame.K_ESCAPE:
					if self.game.active_screen == 'menu screen':
						self.game.is_paused = False
						self.game.active_screen = 'game screen'
					else:
						self.game.is_paused = True
						self.game.active_screen = 'menu screen'	