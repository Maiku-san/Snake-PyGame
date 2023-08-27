import pygame

class Button:
 
    def __init__(self, position_x, position_y, width, height, text_content, clicked):
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.text_content = text_content
        self.clicked = clicked


    def draw(self, surface, font):
        rectangle = pygame.draw.rect(surface, (45, 89, 135), (self.position_x, self.position_y, self.width, self.height))
        
        is_hover_button = self.check_mouse_hover_button(rectangle)
        if is_hover_button is True:
            pygame.draw.rect(surface, (9, 66, 227), (self.position_x, self.position_y, self.width, self.height))
            self.handle_click_event()

        if self.clicked is True:
            pygame.draw.rect(surface, (10, 155, 251), (self.position_x, self.position_y, self.width, self.height))

        # render text content
        text_content_rendered = font.render(self.text_content, True, 'white')
        # get a rectangle for the text content and center it with rectangle defined for the button
        text_rect = text_content_rendered.get_rect(center = (self.position_x + (self.width/2) , self.position_y + (self.height/2)))
        surface.blit(text_content_rendered, text_rect)


    def check_mouse_hover_button(self, button_shape):
        pygame.mouse.get_pos()
        if button_shape.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False
    
    
    def handle_click_event(self):
        btns_pressed = pygame.mouse.get_pressed()
        if btns_pressed[0]:
            self.clicked = True
        else:
            self.clicked = False