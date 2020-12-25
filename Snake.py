import turtle
import numpy as np


class Snake:

    def __init__(self, lenght, height):
        self.grid = np.zeros((height, lenght), dtype=int)
        self.lenght = lenght
        self.height = height

        self.snake_size = 1

    def create_head(self):
        x = self.lenght // 2
        y = self.height // 2
        self.grid[y, x] = 1

    def spawn_food(self):
        spawn = False
        while not spawn:
            y = np.random.randint(0, self.height)
            x = np.random.randint(0, self.lenght)
            if (self.grid[y, x] == 0):
                spawn = True
                self.grid[y, x] = 3

    def eated_food(self):
        
        self.snake_size += 1


if __name__ == '__main__':
    snake = Snake(10, 20)
    snake.create_head()
    snake.spawn_food()
    print(snake.grid)
