from pygame  import *
from random import randint

init()
font.init()

class GameSprite():
    def __init__(self, image_file, x, y, Vx, Vy, w, h):
        self.image = transform.scale( image.load(image_file), (w,h))
        self.rect = self.image.get_rect()
        self.Vx = Vx
        self.Vy = Vy
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.Vy
        if keys[K_DOWN]:
            self.rect.y += self.Vy

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.Vy
        if keys[K_s]:
            self.rect.y += self.Vy

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.Vx
        self.rect.y += self.Vy
        
        if (self.rect.y <= 0):
            self.Vy = randint(5, abs(self.Vy) + 5)
        if (self.rect.y >= win_h):
            self.Vy = -randint(5, abs(self.Vy) + 5)

        global score1, score2, player1, player2, ball

        if sprite.collide_rect(self, player1):
            self.Vx = (randint(5, abs(self.Vx) + 5))
        if sprite.collide_rect(self, player2):
            self.Vx = -randint(5, (abs(self.Vx) + 5))

        if self.rect.x <= 0:
            score2 += 1 
            if  (score2 % 5 == 0 and score2 != 0):
                player2 = Player2("МЕЧЖИДА.png", 705 , 250,0, 10, 100, randint(50, 270)  )
            if  (score2 % 5 != 0 and score2 != 0):
                ball = Ball("nn.png", win_w/2, win_h/2, 5, 5, randint(10, 200), randint(10, 100))
            self.Vx = randint(5, (abs(self.Vx) + 5))

        if self.rect.x >= win_w:
            score1 += 1    
            if (score1 % 5 == 0 and score1 != 0 ):
                player1 = Player1("МЕЧЖИДА.png", 50, 250,0, 10, 100, randint(50, 270)  )
            if  (score1 % 5 != 0 and score1 != 0):
                ball = Ball("nn.png", win_w/2, win_h/2, 5, 5, randint(10, 200), randint(10, 100))
            self.Vx = -randint(5, (abs(self.Vx) + 5))
       
    



win_w, win_h = 800, 600

win = display.set_mode(  (win_w, win_h) )
display.set_caption('Pin Pon')
game = True
finish = False
FPS = 60

score1 = 0
score2 = 0

font0 = font.SysFont('Arial', 50)
clock = time.Clock()

player1 = Player1("МЕЧЖИДА.png", 50, 250,0, 10, 100, 150  )
player2 = Player2("МЕЧЖИДА.png", 705 , 250,0, 10, 100, 150  )
ball = Ball("nn.png", win_w/2, win_h/2, 5, 5, 200, 100)
while game:
    display.update()

    clock.tick(FPS)

    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN and e.key == K_r:            
            player1 = Player1("МЕЧЖИДА.png", 50, 250,0, 10, 100, 300  )
            player2 = Player2("МЕЧЖИДА.png", 705 , 250,0, 10, 100, 300  )
            ball = Ball("nn.png", win_w/2, win_h/2, 5, 5, 100, 50)
            score1 = 0
            score2 = 0
            finish = False

    if not(finish):
        player1.update()
        player2.update()
        ball.update()

        image_score = font0.render('Игрок1:' +str(score1), True, (50, 50, 50))
        image_score2 = font0.render('Игрок2:' +str(score2), True, (50, 50, 50))
        image_win_1 = font0.render("Победил Первый игрок", True, (50, 50, 50))
        image_win_2 = font0.render("Победил Второй игрок", True, (50, 50, 50))
        image_lose = font0.render('Другой проиграл', True, (50, 50, 50))


        win.fill((22,255,255))
        player1.reset()
        player2.reset()
        ball.reset()
        win.blit(image_score, (50, 50))
        win.blit(image_score2, (600, 50))


        if score1 == 50:
            win.blit(image_win_1, (200, 100))
            win.blit(image_lose, (200, 200))
            finish = True
        if score2 == 50:
            win.blit(image_win_2, (200, 100))
            win.blit(image_lose, (200, 200))
            finish = True
