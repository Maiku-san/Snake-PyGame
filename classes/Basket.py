from classes.Fruit import Fruit

class Basket:
	
	def __init__(self, game, snake_1, snake_2, fruit_1):
		self.game = game
		self.snake_1 = snake_1
		self.snake_2 = snake_2
		self.fruits = [fruit_1]

	def of_fruits(self):
		for fruit in self.fruits:
			self.check_fruit(fruit)
			fruit.draw(self.game.screen)

	# deal with fruit eating
	def check_fruit(self, fruit):
		if self.snake_1.is_active == True:
			if self.snake_1.head_position[0] == fruit.position[0] and self.snake_1.head_position[1] == fruit.position[1]:
				self.check_fruit_effect(fruit, self.snake_1)

				self.snake_1.body_position.insert(0, list(self.snake_1.head_position))

				fruit.position, fruit.color = fruit.spawn(self.snake_1.body_position, self.snake_1.is_active, self.snake_2.body_position, self.snake_2.is_active)

		if self.snake_2.is_active == True:
			if self.snake_2.head_position[0] == fruit.position[0] and self.snake_2.head_position[1] == fruit.position[1]:
				self.check_fruit_effect(fruit, self.snake_2)

				self.snake_2.body_position.insert(0, list(self.snake_2.head_position))

				fruit.position, fruit.color = fruit.spawn(self.snake_1.body_position, self.snake_1.is_active, self.snake_2.body_position, self.snake_2.is_active)

	def check_fruit_effect(self, fruit, snake):
		# check fruit effects
			# GREEN FRUIT
			if fruit.color == 'green':
				if snake.color == 'blue':
					self.game.score += 10 * 2
				self.game.score += 10
				# shrink
				for _ in range(5):
					if len(snake.body_position) > 0:
						snake.body_position.pop()
				# get faster!!
				if snake.speed_index != len(snake.speed_options) - 1: 
					snake.speed_index += 1
					snake.speed = snake.speed_options[snake.speed_index]        
					snake.frame_buffer = self.game.fps / snake.speed
			# BLUE FRUIT
			if fruit.color == 'blue':
				if snake.color == 'blue':
					self.game.score += 15 * 2
				self.game.score += 15	 
				snake.color = 'blue'
				snake.time_being_blue = 0
			# YELLOW FRUIT	
			if fruit.color == 'yellow':
				if snake.color == 'blue':
					self.game.score += 25 * 2
				self.game.score += 25
				
				print(f"Ate Yellow Fruit\nfruits in basket: {len(self.fruits)}")
				if len(self.fruits) < 9:
					self.fruits.append(Fruit(self.game.tile_size, self.game.WIDTH, self.game.HEIGHT))
			# RED FRUIT
			if fruit.color == 'red':
				if snake.color == 'blue':	
					self.game.score += 50 * 2
				self.game.score += 25
				# growth spurt
				for _ in range(5):
					snake.body_position.insert(0, list(snake.head_position))
				# slow down
				if snake.speed_index != 1: 
					snake.speed_index -= 1
					snake.speed = snake.speed_options[snake.speed_index]
					snake.frame_buffer = self.game.fps / snake.speed