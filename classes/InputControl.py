import pygame

class InputControl:
	
	def __init__(self, game, snake_1, snake_2):
		self.game = game
		self.snake_1 = snake_1
		self.snake_2 = snake_2


	def handle_input(self):
		# handle events
		for event in pygame.event.get():
			# check if the user clicked x at the top right corner to close the game
			if event.type == pygame.QUIT:
				self.game.check_high_score()
				
				self.game.is_on = False

			# handle buttons
			if self.game.quit_button.clicked is True:
				self.game.check_high_score()

				self.game.is_on = False

			if self.game.play_button.clicked is True:
				self.game.is_paused = False
				self.game.active_screen = 'game screen'
				for i in range(len(self.game.menu_buttons)):
					self.game.menu_buttons[i].clicked = False
		
			if self.game.map_selection_button.check_mouse_hover_button() and event.type == pygame.MOUSEBUTTONDOWN:
				if self.game.active_map == 'Borderless Map':
					self.game.active_map = 'Border Map'
				else:
					self.game.active_map = 'Borderless Map'

			if self.game.green_snake_button.check_mouse_hover_button() and event.type == pygame.MOUSEBUTTONDOWN:
				if self.snake_1.is_active is False:
					self.snake_1.is_active = True
				else:
					self.snake_1.is_active = False
					self.snake_1.change_direction_to = ''
					self.snake_1.is_moving = False
					self.snake_1.head_position, self.snake_1.body_position, self.snake_1.direction = self.snake_1.spawn()

				if self.game.green_snake_button.toggled == False:
					self.game.green_snake_button.toggled = True
				else:
					self.game.green_snake_button.toggled = False
			
			if self.game.yellow_snake_button.check_mouse_hover_button() and event.type == pygame.MOUSEBUTTONDOWN:
				if self.snake_2.is_active is False:
					self.snake_2.is_active = True
				else:
					self.snake_2.is_active = False
					self.snake_2.change_direction_to = ''
					self.snake_2.is_moving = False
					self.snake_2.head_position, self.snake_2.body_position, self.snake_2.direction = self.snake_2.spawn()
				
				if self.game.yellow_snake_button.toggled == False:
					self.game.yellow_snake_button.toggled = True
				else:
					self.game.yellow_snake_button.toggled = False

			# handle keyboard controls
			if event.type == pygame.KEYDOWN:
				if self.game.is_paused is False:
					if event.key == pygame.K_UP:
						self.snake_1.change_direction_to = 'UP'
					if event.key == pygame.K_DOWN:
						self.snake_1.change_direction_to = 'DOWN'
					if event.key == pygame.K_LEFT:
						self.snake_1.change_direction_to = 'LEFT'
					if event.key == pygame.K_RIGHT:
						self.snake_1.change_direction_to = 'RIGHT'

					if event.key == pygame.K_w:
						self.snake_2.change_direction_to = 'UP'
					if event.key == pygame.K_s:
						self.snake_2.change_direction_to = 'DOWN'
					if event.key == pygame.K_a:
						self.snake_2.change_direction_to = 'LEFT'
					if event.key == pygame.K_d:
						self.snake_2.change_direction_to = 'RIGHT'

				# press ESC to bring up menu screen and pause the game
				if event.key == pygame.K_ESCAPE:
					if self.game.active_screen == 'menu screen':
						self.game.is_paused = False
						self.game.active_screen = 'game screen'
					else:
						self.game.is_paused = True
						self.game.active_screen = 'menu screen'	