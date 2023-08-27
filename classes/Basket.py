from classes.Fruit import Fruit

class Basket:
	
	def __init__(self, game, snake_1, fruit_1):
		self.game = game
		self.snake_1 = snake_1
		self.fruits = [fruit_1]

	def of_fruits(self):
		for fruit in self.fruits:
			self.check_fruit(fruit)
			fruit.draw(self.game.screen)

	# deal with fruit eating
	def check_fruit(self, fruit):
		if self.snake_1.head_position[0] == fruit.position[0] and self.snake_1.head_position[1] == fruit.position[1]:
			# check fruit effects
			# GREEN FRUIT
			if fruit.color == 'green':
				if self.snake_1.color == 'blue':
					self.game.score += 10 * 2
				self.game.score += 10
				# shrink
				for _ in range(5):
					if len(self.snake_1.body_position) > 0:
						self.snake_1.body_position.pop()
				# get faster!!
				if self.snake_1.speed_index != len(self.snake_1.speed_options) - 1: 
					self.snake_1.speed_index += 1
					self.snake_1.speed = self.snake_1.speed_options[self.snake_1.speed_index]        
					self.snake_1.frame_buffer = self.game.fps / self.snake_1.speed
			# BLUE FRUIT
			if fruit.color == 'blue':
				if self.snake_1.color == 'blue':
					self.game.score += 15 * 2
				self.game.score += 15	 
				self.snake_1.color = 'blue'
				self.snake_1.time_being_blue = 0
			# YELLOW FRUIT	
			if fruit.color == 'yellow':
				if self.snake_1.color == 'blue':
					self.game.score += 25 * 2
				self.game.score += 25
				
				print(f"Ate Yellow Fruit\nfruits in basket: {len(self.fruits)}")
				if len(self.fruits) < 9:
					self.fruits.append(Fruit(self.game.tile_size, self.game.WIDTH, self.game.HEIGHT))
			# RED FRUIT
			if fruit.color == 'red':
				if self.snake_1.color == 'blue':	
					self.game.score += 50 * 2
				self.game.score += 25
				# growth spurt
				for _ in range(5):
					self.snake_1.body_position.insert(0, list(self.snake_1.head_position))
				# slow down
				if self.snake_1.speed_index != 1: 
					self.snake_1.speed_index -= 1
					self.snake_1.speed = self.snake_1.speed_options[self.snake_1.speed_index]
					self.snake_1.frame_buffer = self.game.fps / self.snake_1.speed

			self.snake_1.body_position.insert(0, list(self.snake_1.head_position))

			fruit.position, fruit.color = fruit.spawn(self.snake_1.body_position)