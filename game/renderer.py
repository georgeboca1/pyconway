import itertools
import pygame

from game.automata import Grid
from game.button import Button


class Game:
    def __init__(self,width,height,window_name) -> None:
        pygame.font.init()

        self.width = width
        self.height = height
        self.window_name = window_name
        self.grid_size = 32
        self.square_size = self.height / self.grid_size
        self.active_squares = []
        self.squares = []
        self.grid = Grid(self.grid_size)
        self.paused = False
        self.drawing = False

        self.screen = pygame.display.set_mode((self.width, self.height),pygame.RESIZABLE | pygame.HWSURFACE)
        pygame.display.set_caption(self.window_name)
        self.clock = pygame.time.Clock()
        self.my_font = pygame.font.SysFont("Arial", 32)
        self.line_width = round(self.grid_size * self.square_size)

        for i in range(self.grid_size):
            self.active_squares.append([0] * self.grid_size)  
        
        for i in range(self.grid_size):
            self.squares.append([0] * self.grid_size)  


        self._draw_grid()

        self.reset_button = Button(
            self.line_width + 20,
            10,
            (self.width - self.line_width) - 35,
            70,
            "RANDOMIZE",
            (92, 204, 187),
            10,
            48
        )
        
        self.pause_button = Button(
            self.line_width + 20,
            90,
            (self.width - self.line_width) - 35,
            70,
            "PAUSE",
            (92, 204, 187),
            10,
            64
        )
        
        self.clear_button = Button(
            self.line_width + 20,
            170,
            (self.width - self.line_width) - 35,
            70,
            "CLEAR",
            (92, 204, 187),
            10,
            64
        )
        
        self.grid_size_button = Button(
            self.line_width + 20,
            250,
            (self.width - self.line_width) - 35,
            70,
            "GRID+",
            (92, 204, 187),
            10,
            64
        )

        self.grid_size_button2 = Button(
            self.line_width + 20,
            330,
            (self.width - self.line_width) - 35,
            70,
            "GRID-",
            (92, 204, 187),
            10,
            64
        )
        


    def restart(self) -> None:
        self.grid = Grid(self.grid_size)

    def start(self) -> None:
        pygame.init()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        print(1)
                        self.restart()

            
            self.handle_mouse_input()

            self.screen.fill("black")
            self.show_grid()
            self.set_grid()
            self.reset_button.update(self.screen, self.restart)
            self.pause_button.update(self.screen, self.set_pause)
            self.clear_button.update(self.screen, self.clear_grid)
            self.grid_size_button.update(self.screen, self.change_grid_size, arg1 = 1)
            self.grid_size_button2.update(self.screen, self.change_grid_size, arg1 = -1)
            if not self.paused:
                self.pause_button.change_color((92, 204, 187))
                self.grid.calculate_neighbor()
            else:
                self.pause_button.change_color((244, 72, 72))

            fps_text = self.my_font.render(str(round(self.clock.get_fps())), False, (255, 255, 0))
            pygame.draw.line(self.screen, (255, 255, 255),(self.line_width,0), (self.line_width, self.height),width=3)

            self.screen.blit(fps_text, (0,0))
            pygame.display.flip()

            self.clock.tick(0)

        pygame.quit()

    def _draw_grid(self) -> None:
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.squares[i][j] = pygame.Rect(
                    j * self.square_size,
                    i * self.square_size,
                    self.square_size + 1,
                    self.square_size + 1
                )
                #text_surface = self.my_font.render(str(self.grid.cells[i][j].active_neighbors), False, (255, 0, 0))
                #self.screen.blit(text_surface, (j*self.square_size,i * self.square_size))

    def show_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                pygame.draw.rect(
                        self.screen,pygame.Color(
                        self.active_squares[i][j] * 255,
                        self.active_squares[i][j] * 255,
                        self.active_squares[i][j] * 255,
                        255
                    ),
                    self.squares[i][j]
                )
    def set_square(self,x,y,value):
        self.grid.cells[x][y].state = value

    def set_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.active_squares[i][j] = self.grid.cells[i][j].state
    
    def handle_mouse_input(self):
        if not self.grid:
            return
        mouse = pygame.mouse.get_pressed()
        for i,j in itertools.product(range(self.grid_size),range(self.grid_size)):
            if self.squares[i][j].collidepoint(pygame.mouse.get_pos()):
                if mouse[0]:
                    self.set_square(i,j,1)
                elif mouse[2]:
                    self.set_square(i,j,0)

    def set_pause(self):
        self.paused = not self.paused

    def clear_grid(self):
        for i,j in itertools.product(range(self.grid_size),range(self.grid_size)):
            self.set_square(i,j,0)

    def change_grid_size(self, direction):
        self.grid_size += 8 * direction 
        if self.grid_size < 1:
            self.grid_size = 1
        print(self.grid_size)
        self.square_size = self.height / self.grid_size

        self.active_squares = []
        self.squares = []

        for i in range(self.grid_size):
            self.active_squares.append([0] * self.grid_size)  
        
        for i in range(self.grid_size):
            self.squares.append([0] * self.grid_size)  
        
        self._draw_grid()
        self.grid = Grid(self.grid_size)
