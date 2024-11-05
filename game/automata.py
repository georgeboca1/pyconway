import itertools
import random

class Cell:
    def __init__(self,x,y) -> None:
        self.x = None
        self.y = None
        self.state = 0
        self.active_neighbors = 0
    
    def compute_state(self) -> None:
        if self.state == 1:
            if self.active_neighbors <= 1:
                self.state = 0
            if self.active_neighbors >= 4:
                self.state = 0
        if self.state == 0 and self.active_neighbors == 3:
            self.state = 1
        
class Grid:
    def __init__(self, size) -> None:
        self.cells = []
        self.size = size
        for i in range(size):
            self.cells.append([])
            for j in range(size):
                self.cells[i].append(Cell(i,j))

        for i in self.cells:
            for j in i:
                if random.randrange(0,5) == 3:
                    j.state = 1
        #self.cells[2][0].state = 1

    def calculate_neighbor(self) -> None:
        #UGLY BUT MORE PERFORMANCE
        for i, j in itertools.product(range(self.size), range(self.size)):
            self.cells[i][j].active_neighbors = 0
            if i >= 1:
                if j >= 1:
                    self.cells[i][j].active_neighbors += self.cells[i-1][j-1].state
                if j < self.size - 1:
                    self.cells[i][j].active_neighbors += self.cells[i-1][j+1].state
                self.cells[i][j].active_neighbors += self.cells[i-1][j].state
            if j >= 1:
                self.cells[i][j].active_neighbors += self.cells[i][j-1].state
            if j < self.size - 1:
                self.cells[i][j].active_neighbors += self.cells[i][j+1].state
            if i < self.size - 1:
                if j < self.size - 1:
                    self.cells[i][j].active_neighbors += self.cells[i+1][j+1].state
                if j >= 1:
                    self.cells[i][j].active_neighbors += self.cells[i+1][j-1].state
                self.cells[i][j].active_neighbors += self.cells[i+1][j].state

        for i in self.cells:
            for j in i:
                j.compute_state()
        #COOL BUT NO PERFORMANCE
        # def update_active_neighbors( i, j, di, dj):
        #     ni, nj = i + di, j + dj
        #     if 0 <= ni < self.size and 0 <= nj < self.size:
        #         self.cells[i][j].active_neighbors += self.cells[ni][nj].state
        # neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


        # for i, j in itertools.product(range(self.size), range(self.size)):
        #     self.cells[i][j].active_neighbors = 0
        #     for di, dj in neighbor_offsets:
        #         update_active_neighbors(i, j, di, dj)

        # for row in self.cells:
        #     for cell in row:
        #         cell.compute_state()


                    
    def print_neighbors(self):
        for i in self.cells:
            for j in i:
                print(j.active_neighbors, end = " ")
            print()


if __name__ == "__main__":
    grid = Grid(8)
    grid.print_neighbors()