import pygame, random

class Snake:

	# speed should be a factor of game.speed
	# factors of 60 are: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60
	speed_options = [5, 6, 10, 12, 15, 20, 30]
	speed_index = 3
	speed = speed_options[speed_index] 
	movement_frame_counter = 0

	# snake is blue
	time_being_blue = 0

	def __init__(self, game, color, is_active):
		self.game = game
		self.color = color
		self.is_active = is_active
		self.head_position, self.body_position, self.direction = self.spawn()
		print(f"snake head: {self.head_position}\nsnake body: {self.body_position}\nsnake facing: {self.direction}")
		self.change_direction_to = ''
		self.is_moving = False
		self.frame_buffer = self.game.fps / self.speed
		
		self.original_color = color

	def update(self):
		if self.is_active:
			if self.color == 'blue' and self.game.is_paused is False:
				self.time_being_blue += 1
			if self.time_being_blue == 600:
				self.time_being_blue = 0
				self.color = self.original_color

			self.movement_frame_counter += 1
			if self.movement_frame_counter == self.frame_buffer:
				self.movement_frame_counter = 0
		
				self.change_direction()
				self.move()
				self.check_collisions()
				
			self.draw()

	def spawn(self):
		spawn_head =  [
			int(random.randint(self.game.tile_size*4, self.game.WIDTH - self.game.tile_size*4) / self.game.tile_size) * self.game.tile_size, 
			int(random.randint(self.game.tile_size*4, self.game.HEIGHT - self.game.tile_size*4) / self.game.tile_size) * self.game.tile_size
			]
		spawn_body = []
		face_direction = ''
		growth_direction = random.randint(0, 3)
		if growth_direction == 0:
			for i in range(1, 4):
				spawn_body.append([spawn_head[0] - (i * 10), spawn_head[1]])
			face_direction = 'RIGHT'
		elif growth_direction == 1:
			for i in range(1, 4):
				spawn_body.append([spawn_head[0] + (i * 10), spawn_head[1]])
			face_direction = 'LEFT'
		elif growth_direction == 2:
			for i in range(1, 4):
				spawn_body.append([spawn_head[0], spawn_head[1] + (i * 10)])
			face_direction = 'UP'
		else:
			for i in range(1, 4):
				spawn_body.append([spawn_head[0], spawn_head[1] - (i * 10)])	
			face_direction = 'DOWN'

		return spawn_head, spawn_body, face_direction
	

	def draw(self):
		# draw head
		pygame.draw.rect(self.game.screen, self.color, [self.head_position[0], self.head_position[1], self.game.tile_size, self.game.tile_size])
		# draw body
		for body_block in self.body_position:
			pygame.draw.rect(self.game.screen, self.color, [body_block[0], body_block[1], self.game.tile_size, self.game.tile_size])

	# snake movement 
	def move(self):

		if self.is_moving is True and self.game.is_paused is False:
			# update body
			self.body_position.insert(0, list(self.head_position))
			self.body_position.pop()

			# update head position according to snake's direction
			if self.direction == 'UP':
				self.head_position[1] -= 10
			if self.direction == 'DOWN':				
				self.head_position[1] += 10
			if self.direction == 'LEFT':
				self.head_position[0] -= 10
			if self.direction == 'RIGHT':
				self.head_position[0] += 10	

	# snake direction changes
	def change_direction(self):	
		# prevent the snake to change to a direction that is directly opposite of the current facing direction
		if self.change_direction_to == 'UP' and self.direction != 'DOWN':
			self.direction = 'UP'
			self.is_moving = True
		if self.change_direction_to == 'DOWN' and self.direction != 'UP':
			self.direction = 'DOWN'
			self.is_moving = True
		if self.change_direction_to == 'LEFT' and self.direction != 'RIGHT':
			self.direction = 'LEFT'
			self.is_moving = True
		if self.change_direction_to == 'RIGHT' and self.direction != 'LEFT':
			self.direction = 'RIGHT'
			self.is_moving = True

	def check_collisions(self):
		# on snake body
		for block in self.body_position:
			if self.head_position[0] == block[0] and self.head_position[1] == block[1]:
				self.change_direction_to = ''
				self.is_moving = False
				self.color = 'gray'

				self.game.check_high_score()
				self.game.score = 0
				return True
		
		# on map with no borders there are no border collision, so the snake just "teleports" to the opposite side of the map
		if self.game.active_map == 'Borderless Map':
			if self.head_position[0] < 0:
				self.head_position[0] = self.game.WIDTH - self.game.tile_size
				return False
			if self.head_position[0] > self.game.WIDTH - self.game.tile_size:
				self.head_position[0] = 0
				return False
			if self.head_position[1] < 0:
				self.head_position[1] = self.game.HEIGHT - self.game.tile_size
				return False
			if self.head_position[1] > self.game.HEIGHT - self.game.tile_size:
				self.head_position[1] = 0
				return False

		# on map borders for map_1	
		if self.game.active_map == 'Border Map':
			if self.head_position[0] < 0 or self.head_position[0] > self.game.WIDTH - self.game.tile_size:
				self.change_direction_to = ''
				self.is_moving = False
				self.color = 'gray'

				self.game.check_high_score()
				self.game.score = 0
				return True
			if self.head_position[1] < 0 or self.head_position[1] > self.game.HEIGHT - self.game.tile_size:
				self.change_direction_to = ''
				self.is_moving = False
				self.color = 'gray'

				self.game.check_high_score()
				self.game.score = 0
				return True
		
		return False