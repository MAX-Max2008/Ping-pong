from pygame import *
from random import randint
font.init()

dopspeed_min = 0.05
win_width = 1400
win_height = 900

window = display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')
#background = transform.scale(image.load('tenis_ball.png'), (win_width, win_height))
background = transform.scale(image.load('rx0pgnkyqn4853e48aq6teedmtaixz2q.jpg'), (win_width, win_height))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 820:
            self.rect.y += self.speed

    def move_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 820:
            self.rect.y += self.speed

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 1370, 200, 4, 50, 150)
ball = GameSprite('tetenis_ball.png', 700, 450, 4, 25, 75)

font = font.Font(None, 35)
win1 = font.render('Левый победил!', True, (73, 255, 0))
win2 = font.render('Правый победил!', True, (73, 255, 0))