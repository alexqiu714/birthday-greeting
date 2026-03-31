import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill("black")

cake = pygame.image.load("Lesson 3 - Brithday Greeting/images/cake.jpg") 
cupcake = pygame.image.load("Lesson 3 - Brithday Greeting/images/cupcake.jpg")
cupcake1 = pygame.transform.scale(cupcake, (500,500))

cake1 = pygame.transform.scale(cake, (500,500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(cupcake1, (0,0))
    pygame.display.update()