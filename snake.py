#collision with herself

import random
import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

WIN_WIDTH = 600
WIN_HEIGHT = 600

RECT_DIM = 20

BLACK = (0,0,0)
RED = (255, 0, 0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)

LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'

pygame.font.init()

SCORE_FONT = pygame.font.SysFont("monospace", 25)
GAME_OVER_FONT = pygame.font.SysFont("monospace", 50)
OVERTEXT = GAME_OVER_FONT.render("Game Over", 1, WHITE)
CONTINUETEXT1 = GAME_OVER_FONT.render("Press Enter", 1, WHITE)
CONTINUETEXT2 = GAME_OVER_FONT.render("to start again", 1, WHITE)

FPS = 10

class Snake:
    def __init__(self):
        self.x = WIN_WIDTH-100
        self.y = 300
        self.tail = [(self.x+RECT_DIM, self.y), (self.x+2*RECT_DIM, self.y)]
        self.len = 3
        self.dir = LEFT
        self.food = Food()
    
    def draw(self,win):
        pygame.draw.rect(win, GREEN, (self.x, self.y, RECT_DIM, RECT_DIM))
        for part in self.tail:
          pygame.draw.rect(win, GREEN, (part[0], part[1], RECT_DIM, RECT_DIM))
        self.food.draw(win)
    
    
    def move(self):
        for i in reversed(range(1, self.len-1)):
                self.tail[i] = self.tail[i-1]
        self.tail[0] = (self.x, self.y)

        if self.dir == LEFT:
            self.x-=RECT_DIM

        if self.dir == RIGHT:
            self.x+=RECT_DIM

        if self.dir == UP:
            self.y-=RECT_DIM

        if self.dir == DOWN:
            self.y+=RECT_DIM


    def grow(self):
        last = self.tail[(self.len)-2]
        if last[0] == self.x:
            if last[1] > self.y: #end in below head
                pos = (last[0], last[1]+RECT_DIM)
            else: #end is above head
                pos = (last[0], last[1]-RECT_DIM)

        if last[0] < self.x:
            if last[1] == self.y: #moving to right
                pos = (last[0]-RECT_DIM, last[1])
            if last[1] > self.y: #
                pos = (last[0]-RECT_DIM, last[1])
            if last[1] < self.y:
                pos = (last[0], last[1]- RECT_DIM)
        
        if last[0] > self.x:
            if last[1] == self.y:# moving to left
                pos = (last[0] + RECT_DIM, last[1])
            if last[1] > self.y:
                pos = (last[0] + RECT_DIM, last[1])
            if last[1] < self.y:
                pos = (last[0], last[1] - RECT_DIM)

     
        self.tail.append(pos)
        self.len+=1
        self.food = Food()
    
    def eat(self,win):
        snake_rect = pygame.draw.rect(win,GREEN, (self.x, self.y, RECT_DIM,RECT_DIM))
        food_rect = pygame.draw.rect(win, RED, (self.food.x, self.food.y, RECT_DIM, RECT_DIM))
        if snake_rect.colliderect(food_rect):
            self.grow()
            return True
    
    def die(self, win):
        if self.x + RECT_DIM > WIN_WIDTH or self.x < 0 or self.y < 0 or self.y + RECT_DIM > WIN_HEIGHT: #borders
            return True
        head = (self.x, self.y, RECT_DIM, RECT_DIM)
        head_rect = pygame.draw.rect(win, WHITE, head)
        for i in range (1, self.len-2):
            tail_rect = pygame.draw.rect(win, WHITE, (self.tail[i][0], self.tail[i][1], RECT_DIM, RECT_DIM))
            if head_rect.colliderect(tail_rect):
                return True

     #  for part in self.tail:
     
    def handle_keydown(self, key):
        if key == pygame.K_UP:
            if self.dir == DOWN:
                return
            else:
                self.dir = UP
        if key == pygame.K_DOWN:
            if self.dir == UP:
                return
            else:
                self.dir = DOWN  
        if key == pygame.K_LEFT:
            if self.dir == RIGHT:
                return
            else:
                self.dir = LEFT
        if key == pygame.K_RIGHT:
            if self.dir == LEFT:
                return
            else:
                self.dir = RIGHT



class Food:
    def __init__(self):
        random.seed(time.time())
        self.x = random.randrange(40, WIN_WIDTH-50)
        self.y = random.randrange(40, WIN_WIDTH-50)
    
    def draw(self,win):
        pygame.draw.rect(win, RED, (self.x, self.y, RECT_DIM, RECT_DIM))


def draw_window(win, snake, score):
    snake.draw(win)
    scoretext = SCORE_FONT.render("Score = "+str(score), 1, WHITE)
    win.blit(scoretext, (5,10))
    pygame.display.update()

def game_over(win, score):
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return False
        win.fill(BLACK)
        scoretext = GAME_OVER_FONT.render("Score = "+str(score), 1, WHITE)
        win.blit(scoretext, (WIN_WIDTH/2-WIN_WIDTH/4,WIN_HEIGHT/3))
        win.blit(OVERTEXT, (WIN_WIDTH/2-WIN_WIDTH/4,WIN_HEIGHT/6))
        win.blit(CONTINUETEXT1, (WIN_WIDTH/2-WIN_WIDTH/4,WIN_HEIGHT/2))
        win.blit(CONTINUETEXT2, (WIN_WIDTH/2-WIN_WIDTH/4-50,WIN_HEIGHT/2+75))
        pygame.display.update()

def main():
    run = True
    while run:
        clock = pygame.time.Clock()
        play = True
        pygame.init()
        snake = Snake()
        score = 0
        win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Snake')
        while play:
            clock.tick(FPS)
            win.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    snake.handle_keydown(event.key)
            snake.move()
            if snake.eat(win):
                score+=1
            if snake.die(win):
                play = False
            draw_window(win, snake, score)
        if not play and run:
            if game_over(win, score):
                run = False
    
    pygame.quit()   
    quit()

if __name__ == '__main__':
    main()
    