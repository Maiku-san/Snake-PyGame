# import libraries
import pygame
# import classes
from classes.Basket import Basket
from classes.Fruit import Fruit
from classes.Game import Game
from classes.InputControl import InputControl
from classes.Snake import Snake

pygame.init()

# fonts for text in game
list_of_fonts = [
	pygame.font.SysFont("impact", 20), # 0
	pygame.font.SysFont("impact", 40)  # 1
	]

# class instances
game = Game(list_of_fonts)
snake_1 = Snake(game, 'green')
input_control = InputControl(game, snake_1)
fruit_1 = Fruit(game.tile_size, game.WIDTH, game.HEIGHT)
basket = Basket(game, snake_1, fruit_1)

# game loop
while game.is_on:
	game.screen.fill('black')
	game.timer.tick(game.fps)

	# display scores
	game.show_high_score()
	game.show_score()

	# handle game inputs
	input_control.handle_input()
	# handle player
	snake_1.update()
	# handle fruit
	basket.of_fruits()
	# show game screens
	game.show_screen()

	pygame.display.flip()

pygame.quit()  

quit()