from pygame  import *
init()
font.init()

class GameSprite():
    def __init__(self, image_file, x, y, Vx, Vy, w, h):
        self.image = transform.scale( image.load(image_file), (w,h))
        self.rect = self.image.get_rect()
        self.Vx = Vx
        self.Vy = Vy
        self.x = x
        self.y = y
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

win_w, win_h = 800, 600

win = display.set_mode(  (win_w, win_h) )
game = True
finish = False
FPS = 60

font0 = font.SysFont('Arial', 50)
clock = time.Clock()

player1 = Player1("nn.jpg", 50, 300,0, 10, 20, 100  )

while game:
    display.update()

    clock.tick(FPS)

    for e in event.get():
        if e.type == QUIT:
            game = False

    win.fill((0,0,0))
    player1.reset()