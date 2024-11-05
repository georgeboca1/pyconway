# Conway's Game of Life Simulation

A personal project that simulates Conway's Game of Life using Python and Pygame. This project serves as a portfolio piece and demonstrates my skills in Python programming, game development with Pygame, and "optimized" algorithm design.

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Things I’ve Learned](#things-ive-learned)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Future Improvements](#future-improvements)


## About the Project

Conway's Game of Life is a zero-player game that demonstrates cellular automata, where cells on a grid evolve based on simple rules. The simulation creates complex behaviors from simple beginnings, and this project brings it to life using Pygame.

## Features

- **Dynamic Grid Simulation**: Watch the evolution of cells over time with adjustable grid sizes.
- **Pattern Creation**: Create various starting patterns (like gliders, oscillators, etc.) or random cell arrangements.
- **Pause and Reset**: Pause the game to examine patterns and reset to start fresh.

## Things I’ve Learned

This project helped me deepen my knowledge in several key areas:
- **Python and Pygame**: Enhanced my Pygame skills, learning how to handle events, rendering, and game loops.
- **UI**: Experimented with created a UI from the grounds up with no direct help from a framework.
- **Data Structures**: Explored efficient data structures to represent and update the cell grid, keeping memory usage low.
- **Software Design**: Improved my understanding of structuring code for clarity and modularity, making the project easier to extend or modify.
- **Object Oriented Approach**: Learned how to make a project more readable with the use of classes, inheritance and more.

## Requirements

- **Python** 3.6+
- **Pygame** library

Install Pygame using:
```bash
pip install pygame
```

## How to Run
Clone the repository:
```bash
git clone https://github.com/yourusername/conway-game-of-life.git
```
Navigate into the project directory:
```bash
cd conway-game-of-life
```
Run the simulation:
```bash
python game_of_life.py
```

## Usage
- **Start/Stop Simulation**: Click the button on the right to pause and unpause the simulation.
- **Add/Remove Cells**: Click on cells in the grid to manually toggle them as alive or dead.
- **Randomize the grid**: Click on the randomize button to randomize your grid.
- **Change grid size**: Change the grid size to create more space for your art.

## Future improvements 
- **Frame independent speed** - Currently the simulation runs on the speed of your computer, this means that the more FPS you have, the faster the simulation runs. Redo the simulation's logic so that we can have more calculations or less per frame.
- **UI responsiveness** - I created a bare-minimum UI that does not currently interact with window changes, doing it would be overkill for a small project.
- **Optimization** - There are various improvements that can be done to the code, most obvious one is to not draw black squares at all.
