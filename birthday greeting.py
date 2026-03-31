import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill("black")

cake = pygame.image.load("Lesson 3 - Brithday Greeting/images/cake.jpg") 
cupcake = pygame.image.load("Lesson 3 - Brithday Greeting/images/cupcake.jpg")
cupcake1 = pygame.transform.scale(cupcake, (500,500))
birthday = pygame.image.load("Lesson 3 - Brithday Greeting/images/birthday.jpg")
hat = pygame.image.load("Lesson 3 - Brithday Greeting/images/hat.jpg")

cake1 = pygame.transform.scale(cake, (500,500))
birthday1 = pygame.transform.scale(birthday, (500,500))
hat1 = pygame.transform.scale(hat, (500,500))

print(pygame.font.get_fonts())
font = pygame.font.SysFont("arial", 25)
font1 = pygame.font.SysFont("sathu", 30)
font2 = pygame.font.SysFont("didot", 30)
font3 = pygame.font.SysFont("ptserif", 30)
text = font.render("Happy Birthday", True, "yellow")
text1 = font1.render("Wish you luck", True, "light green")
text2 = font2.render("Have a blast", True, "purple")
text3 = font3.render("Enjoy your day", True, "orange")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(cupcake1, (0,0))
    screen.blit(text, (225, 50))
    pygame.display.update()
    pygame.time.wait(2000)
    screen.blit(cake1, (0,0))
    screen.blit(text1, (200, 50))
    pygame.display.update()
    pygame.time.wait(2000)
    screen.blit(birthday1, (0,0))
    screen.blit(text2, (200, 50))
    pygame.display.update()
    pygame.time.wait(2000)
    screen.blit(hat1, (0,0))
    screen.blit(text3, (200, 50))
    pygame.display.update()
    pygame.time.wait(2000)