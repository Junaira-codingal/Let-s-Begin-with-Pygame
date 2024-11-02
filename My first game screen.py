import pygame
pygame.init()
olive = (70,90,24)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600,600))

pygame.display.set_caption('Image')

image = pygame.image.load('gimage.jpg')

DEFAULT_IMAGE_SIZE = (250,250)

image = pygame.transform.scale(image,DEFAULT_IMAGE_SIZE )

DEFAULT_IMAGE_POSITION = (170,170)

while True:
    
    screen.fill(olive)
    screen.blit(image,DEFAULT_IMAGE_POSITION)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
            quit()
            
    pygame.display.flip()
    clock.tick(30)
    