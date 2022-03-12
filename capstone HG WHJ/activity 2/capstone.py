import pygame
pygame.init()

golden1 = (183,110,121)
color2 =(175,238,238)

clock = pygame.time.Clock()

width=600
height=400
x= 100
y= 15
#speed 
dx=0
dy=2

x1= 200
y1=335
#speed
dx1=0
dy1=2

screen = pygame.display.set_mode((width,height))
img = pygame.image.load("pic.jpeg").convert()
pygame.display.set_caption("Bouncing balls")

while True:
   # screen.fill((255,199,203))
    screen.blit(img,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
           
    x+=dx
    y+=dy
     
     # check boundary of canvas
    if y<0 or y>height-20:
         dy*=-1
    if x<0 or x>width-20:
         dx*=-1
             
     # second ball movement
     
    x1+=dx1
    y1+=dy1
      
     # check boundry for second ball
    if y1<0 or y1>height-20:
         dy1*=-1
    if x1<0 or x1>width-20:
             dx1*=-1        
    pygame.draw.circle(screen , golden1 , (x,y), 20)
    pygame.draw.circle(screen , color2 , (x1,y1), 20)
    clock.tick(300)
    
    pygame.display.update()

