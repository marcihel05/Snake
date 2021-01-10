import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random

WIN_WIDTH = 800
WIN_HEIGHT = 800

BLACK = (0,0,0)
RED = (255, 0, 0)
WHITE = (255,255,255)

LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'

class Snake:
    def __init__(self):
        self.x = 600
        self.y = 300
        self.tail = [(self.x+20, self.y), (self.x+40, self.y)]
        self.len = 3
        self.dir = LEFT
    def draw(self,win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, 20, 20))
        for i in range (0, self.len-1):
            pygame.draw.rect(win, WHITE, (self.tail[i][0], self.tail[i][1], 20, 20))
    def move(self):


    def add_tail(self):
        self.tail[self.len] = ()
        self.len+=1


class Food:
    def __init__(self):
        self.x = random.randrange(40, 780)
        self.y = random.randrange(40, 780)
    #def draw(self,win):

def handle_keydown(key):
    if key == pygame.K_UP:

    if key == pygame.K_DOWN:

    if key == pygame.K_LEFT:

    if key == pygame.K_RIGHT:


def draw_window(win, snake, food):
    snake.draw(win)
    pygame.draw.rect(win, RED, (food.x, food.y, 20, 20))
    pygame.display.update()

def main():
    run = True
    while run == True:
        play = True
        pygame.init()
        snake = Snake()
        food = Food()
        win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        win.fill(BLACK)
        pygame.display.set_caption('Snake')
        while play == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    handle_keydown(event.key)
            
            draw_window(win, snake, food)
    pygame.quit()      
    
                
        


if __name__ == '__main__':
    main()
    