import pygame, random

class Fruit:

	def __init__(self, tile_size, window_WIDTH, window_HEIGHT):
		self.tile_size = tile_size
		self.window_WIDTH = window_WIDTH
		self.window_HEIGHT = window_HEIGHT
		self.position = self.get_fruit_position()
		self.color = random.choice(['red', 'green', 'blue', 'yellow'])
		print(f"fruit position: {self.position}")


	def get_fruit_position(self):
		return [
			int(random.randint(self.tile_size, self.window_WIDTH - self.tile_size*2) / self.tile_size) * self.tile_size, 
			int(random.randint(self.tile_size, self.window_HEIGHT - self.tile_size*2) / self.tile_size) * self.tile_size
			]
	
	def spawn(self, snake_1_body_position, snake_1_is_active, snake_2_body_position, snake_2_is_active):
		fruit_position = self.get_fruit_position()
		fruit_color = random.choice(['red', 'green', 'blue', 'yellow'])

		# while fruit_position in snake_1_body_position or fruit_position in snake_2_body_position:
		# 	print("fruit attempted to spawn in a position occupied by a snake's body")
		# 	fruit_position = self.get_fruit_position()
		while True:
			if snake_1_is_active and fruit_position in snake_1_body_position:
				fruit_position = self.get_fruit_position()
				continue
			if snake_2_is_active and fruit_position in snake_2_body_position:
				fruit_position = self.get_fruit_position()
				continue 

			break

		return fruit_position, fruit_color
	
	def draw(self, surface):
		# draw fruit
		pygame.draw.rect(surface, self.color, [self.position[0], self.position[1], self.tile_size, self.tile_size])