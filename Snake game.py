import pygame
import random
import time
import sys

pygame.init()

class Snake():

    def __init__(self):
        self.position = [100, 50] 
        self.body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50]]
        self.dir = "DOWN" 

    def move(self, foodpos):
        if self.dir == "DOWN":
            self.position[1] += 10
            
        if self.dir == "UP":
            self.position[1] -= 10
            
        if self.dir == "RIGHT":
            self.position[0] += 10
            
        if self.dir == "LEFT":
            self.position[0] -= 10
            
        self.body.insert(0, list(self.position))

        if self.position == foodpos:
            return 1

        else:
            self.body.pop()
            return 0

    def collide(self):
        if self.position[0] < 0 or self.position[0] > 500:
            return 1
        if self.position[1] < 0 or self.position[1] > 500:
            return 1
        for body in self.body:
            if self.position[0] == body[0] and self.position[1] == body[1]:
                return 0

        return 0

class Food():

    def __init__(self):
        self.f_position = [random.randint(4, 46)*10, random.randint(4, 46)*10]
        self.foodonscreen = True

    def spawnfood(self):
        if self.foodonscreen == False:
            self.f_position = [random.randint(4, 46)*10, random.randint(4, 46)*10]
            self.foodonscreen = True
        return self.f_position


weidth = 500
height = 500
screen = (weidth, height)
window = pygame.display.set_mode(screen)

snake = Snake()
food = Food()

score = 0

running = True


def gameover():
    time.sleep(3)
    pygame.quit()
    sys.exit()

while running:
    pygame.time.delay(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.dir = "DOWN"
            if event.key == pygame.K_UP:
                snake.dir = "UP"
            if event.key == pygame.K_RIGHT:
                snake.dir = "RIGHT"
            if event.key == pygame.K_LEFT:
                snake.dir = "LEFT"



    foodpos = food.spawnfood()
    if (snake.move(foodpos) == 1):
        food.foodonscreen = False
        score += 1

    window.fill((0, 0, 0))
    for rect in snake.body:
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(rect[0], rect[1], 10, 10))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(foodpos[0], foodpos[1], 10, 10))
    if (snake.collide() == 1):
        gameover()
    pygame.display.update()
    pygame.display.set_caption('Snake game   score-'+str(score))

pygame.quit()
