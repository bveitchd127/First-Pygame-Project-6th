import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True




class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.health = 10
        self.color = color
    
    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w]):
            self.y -= 4
        elif (keys[pygame.K_s]):
            self.y += 4
        
        if (keys[pygame.K_a]):
            self.x -= 4
        elif (keys[pygame.K_d]):
            self.x += 4
    
    def draw(self, screen):
        playerRect = pygame.Rect(self.x, self.y, 60, 100)
        pygame.draw.rect(screen, self.color, playerRect)

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 4
        self.color = "red"
    
    def update(self, player):
        # Enemy update needs player, since it's targeting player

        enemyToPlayer = pygame.math.Vector2( (player.x - self.x, player.y - self.y) )
        enemyToPlayer.scale_to_length(3)
        
        self.x += enemyToPlayer.x
        self.y += enemyToPlayer.y


    def draw(self, screen):
        # Make a rectangle at position of enemy, and size 40 by 60
        enemyRect = pygame.Rect(self.x, self.y, 40, 60)
        # Draw the rectangle on the screen
        pygame.draw.rect(screen, self.color, enemyRect)



p1 = Player(200, 100, "blue")
e1 = Enemy(800, 500)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    p1.update()
    e1.update(p1)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark green")

    # Painting our player
    p1.draw(screen)
    e1.draw(screen)




    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
