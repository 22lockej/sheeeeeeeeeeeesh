import pygame
import pygame_menu
pygame.init()
surface = pygame.display.set_mode((600, 400))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    pass
    

menu = pygame_menu.Menu(300, 400, 'Welcome',
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game )
menu.add.button('Quit', pygame_menu.events.EXIT)
class Game:
    screen = None
    invaders = []
    rockets = []
    lost = False
    bulletspeed = -2

    def __innit__(self, width, height):
        pygame.init()
        self.bulletspeed = -2
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False

        hero = Hero(self, width / 2, height - 20)
        generator = Generator(self)
        rocket = None

        while not done:
            menu.mainloop(surface)
            if len(self.invaders) == 0:
                self.displayText("PRESS ENTER TO CONTINUE")
                self.bulletspeed -= 1
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_RETURN]:
                        invader.draw()
                        invader(game, x, y)
                        
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]: 
                hero.x -= 2 if hero.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:  
                hero.x += 2 if hero.x < width - 20 else 0 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(Rocket(self, hero.x, hero.y, self.bulletspeed))

            #self.rockets.append(Rocket(self, hero.x, hero.y, 8))
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for invader in self.invaders:
                invader.draw()
                invader.checkCollision(self)
                if (invader.y > height):
                    self.lost = Trues 
                    self.displayText("YOU DIED")

            for rocket in self.rockets:
                rocket.draw()
                 

            if not self.lost: hero.draw()

    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (44, 0, 62))
        self.screen.blit(textsurface, (110, 160))


class invader:
    def __init__(self, game, x, y):
        self.image = pygame.image.load('duende.png')
        self.x = x
        self.game = game
        self.y = y
        self.size = 30

    #self.image = pygame.image.load("invaderdude.png")
    def draw(self):
        self.game.screen.blit(self.image,(self.x, self.y))
        self.y += 0.2


        

    def checkCollision(self, game):
        for rocket in game.rockets:
            if (rocket.x < self.x + self.size and
                    rocket.x > self.x - self.size and
                    rocket.y < self.y + self.size and
                    rocket.y > self.y - self.size):
                game.rockets.remove(rocket)
                game.invaders.remove(self)


class Hero:
    def __init__(self, game, x, y):
        self.image = pygame.image.load('sprite_0.png')
        self.x = x
        self.game = game
        self.y = y

    def draw(self):
        self.game.screen.blit(self.image,(self.x, self.y))


class Generator:
    def __init__(self, game):
        margin = 0
        width = 50
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.invaders.append(invader(game, x, y))

      


class Rocket:
    def __init__(self, game, x, y, speed):
        self.image = pygame.image.load('bala.png')
        self.x = x
        self.y = y
        self.game = game
        self.speed = speed
        

        
    def draw(self):
        self.game.screen.blit(self.image,(self.x, self.y))  
        self.y += self.speed
        

if __name__ == '__main__': 
    game = Game(600, 400)