from pygame import *
from random import randint
font.init()

dopspeed_min = 10
win_width = 1400
win_height = 900

ball_speed_x = 7
ball_speed_y = 7

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

racket1 = Player('racket.png', 30, 200, 12, 100, 300)
racket2 = Player('racket.png', 1300, 200, 12, 100, 300)
ball = GameSprite('tenis_ball.png', 700, 450, 4, 110, 110)

font = font.Font(None, 90)
win1 = font.render('Левый победил!', True, (73, 255, 0))
win2 = font.render('Правый победил!', True, (73, 255, 0))

gayme = True
finish = False
clock = time.Clock()
FPS = 60

while gayme:
    for e in event.get():
        if e.type == QUIT:
            gayme = False
    if not finish:
        window.blit(background, (0, 0))
        racket1.move_left()
        racket1.reset()
        racket2.move_right()
        racket2.reset()
        ball.reset()
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
        if ball_speed_y > 0:
            ball.rect.y += dopspeed_min
        if ball_speed_y < 0:
            ball.rect.y -= dopspeed_min
        if ball_speed_x > 0:
            ball.rect.x += dopspeed_min
        if ball_speed_x < 0:
            ball.rect.x -= dopspeed_min
        if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
            ball_speed_x *= -1
            ball_speed_y *= 1
        if ball.rect.y > win_height - 50:
            ball_speed_y *= -1
        if ball.rect.y < 0:
            ball_speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(win2, (500, 300))
        if ball.rect.x > win_width:
            finish = True
            window.blit(win1, (500, 300))
        display.update()
    time.delay(60)