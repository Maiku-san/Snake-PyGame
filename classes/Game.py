import pygame
from classes.Button import Button

class Game:

	# game window dimensions
	WIDTH, HEIGHT = 800, 600
	# game window and window caption
	screen = pygame.display.set_mode([WIDTH, HEIGHT])
	pygame.display.set_caption('Snake Python Game ^_^')

	# tile size for the game, for example it can be used to define each block of the snake's body
	tile_size = 10
	score = 0

	# high score read in from text file
	highscore_file = open('SnakeHighScore.txt', 'r')
	read_highscore_file = highscore_file.readlines()
	high_score = int(read_highscore_file[0])
	highscore_file.close()
	
	# timer and framerate to control the speed at which the game runs
	timer = pygame.time.Clock()
	fps = 60

	# scenarios
	active_map = 'Borderless Map'
	# active screen
	active_screen = "menu screen"
	# menu screen surface
	##menu_surface = pygame.Surface((400, 400), pygame.SRCALPHA)	# per-pixel alpha
	##menu_surface.fill((107, 107, 107, 128)) # 4th argument for alpha value
	menu_surface = pygame.Surface((400, 400))
	menu_surface.set_alpha(128)
	menu_surface.fill((107, 107, 107))

	# buttons
	play_button = Button(250, 200, 300, 55, 'Play', False)
	map_selection_button = Button(250, 265, 300, 55, 'Border', False)
	quit_button = Button(250, 330, 300, 55, 'Quit', False)
	menu_buttons = [play_button, map_selection_button, quit_button]

	def __init__(self, list_of_fonts):
		self.is_on = True
		self.is_paused = True
		self.list_of_fonts = list_of_fonts
		

	def show_screen(self):
		match self.active_screen:
			case "game screen":
				if self.active_map == 'Border Map':
					self.show_map_1()
			case "menu screen":
				self.show_menu_screen()
			case _:
				print("default case")


	def show_map_1(self):
		# draw a border around the screen, 10 pixels into the interior
		pygame.draw.rect(self.screen, (107, 107, 107), [0, 0, self.WIDTH, self.HEIGHT], self.tile_size)


	def show_menu_screen(self):
		# background rectangle for menu screen
		self.screen.blit(self.menu_surface, (200, 100))
		# buttons on menu
		self.play_button.draw(self.screen, self.list_of_fonts[1])
		self.quit_button.draw(self.screen, self.list_of_fonts[1])
		# map switch button to select border/no border
		self.map_selection_button.draw(self.screen, self.list_of_fonts[1])
		if self.active_map == 'Border Map':
			pygame.draw.rect(self.screen, 'green', (250, 265, 300, 55), 5)

		


	def show_score(self):
		score_text_surface = self.list_of_fonts[0].render(f"SCORE: {self.score}", True, 'white') 
		## score_text_surface.set_alpha(200)	# changes score text transparency with alpha	
		score_rect = score_text_surface.get_rect(center = (self.WIDTH/2, self.HEIGHT - 2*self.tile_size))

		self.screen.blit(score_text_surface, score_rect)

	def show_high_score(self):
		high_score_text_surface = self.list_of_fonts[0].render(f"HIGH SCORE: {self.high_score}", True, 'white')
		high_score_rect = high_score_text_surface.get_rect(center = (self.WIDTH/2, 2*self.tile_size))

		self.screen.blit(high_score_text_surface, high_score_rect)

	def check_high_score(self):
		if self.score > self.high_score:
			self.high_score = self.score
			file = open('SnakeHighScore.txt', 'w')
			file.write(str(self.high_score))
			file.close()