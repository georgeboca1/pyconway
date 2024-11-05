import pygame

class Button:
    def __init__(self, x, y, w, h, text, color, radius,font_size) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.color = color
        self.current_color = self.color
        self.radius = radius
        self.font_size = font_size

        self.font = pygame.font.SysFont("Candara",self.font_size)
        self.text_x = self.x + (self.w/2) - (self.font.size(self.text)[0]/2)
        self.text_y = self.y + (self.h/2) - (self.font.size(self.text)[1]/2)
        self.pressed = False

    def update(self,screen, action, **kwargs):
        pygame.draw.rect(screen,self.current_color,(self.x,self.y,self.w,self.h), border_radius=self.radius)
        self.font.render(self.text, True, (0,0,0))
        
        if self.x < pygame.mouse.get_pos()[0] < self.x + self.w and self.y < pygame.mouse.get_pos()[1] < self.y + self.h:
            self.current_color = (self.color[0] + 10, self.color[1] + 10, self.color[2] + 10)
            if pygame.mouse.get_pressed()[0]:
                self.current_color = (self.color[0] - 30, self.color[1] - 30, self.color[2] - 30)
                if not self.pressed:
                    if len (kwargs) > 0:
                        action(kwargs["arg1"])
                    else:
                        action()
    
                self.pressed = True
            else:
                self.pressed = False 
            
        else:
            self.current_color = self.color

        screen.blit(self.font.render(self.text, True, (0,0,0)), (self.text_x, self.text_y))
    def change_color(self,color):
        self.color = color