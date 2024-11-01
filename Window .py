import pygame

pygame.init()

screen = pygame.display.set_mode((400,300))
color = (247 , 79 , 100)

screen.fill(color)

done = False
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    pygame.display.flip()