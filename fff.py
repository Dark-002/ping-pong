from pygame  import *
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
        if (self.rect.y <= 0) or (self.rect.y >= win_h):
            self.Vy = -self.Vy
        if sprite.collide_rect(self, player1):
            self.Vx = abs(self.Vx)
        if sprite.collide_rect(self, player2):
            self.Vx = -abs(self.Vx)
        if self.rect.x <= 0:
            'плюс один к игроку2'
        if self.rect.x >= win_w:
            "плюс один к игроку1"


win_w, win_h = 800, 600

win = display.set_mode(  (win_w, win_h) )
display.set_caption('Pin Pon')
game = True
finish = False
FPS = 60

font0 = font.SysFont('Arial', 50)
clock = time.Clock()

player1 = Player1("МЕЧЖИДА.png", 50, 250,0, 10, 50, 200  )
player2 = Player2("МЕЧЖИДА.png", 705 , 250,0, 10, 50, 200  )
ball = Ball("nn.png", win_w/2, win_h/2, 5, 5, 100, 50)
while game:
    display.update()

    clock.tick(FPS)

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    player1.update()
    player2.update()
    ball.update()

    win.fill((22,255,255))
    player1.reset()
    player2.reset()
    ball.reset()
