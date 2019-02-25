from pygame import gfxdraw
import sys,pygame
pygame.init()

screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))
pygame.display.flip()

white=(255,255,255)

def midptellipse(rx, ry, xc, yc): 
    x = 0
    y = ry 
  
    # Initial decision parameter of region 1 
    d1 = (ry * ry) - (rx * rx * ry) +  (0.25 * rx * rx)
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y 
  
    # For region 1 
    while (dx < dy):
        # Print points based on 4-way symmetry
        gfxdraw.pixel(screen,round(x+xc),round(y+yc),white)
        gfxdraw.pixel(screen,round(-x+xc),round(y+yc),white)
        gfxdraw.pixel(screen,round(x+xc),round(-y+yc),white)
        gfxdraw.pixel(screen,round(-x+xc),round(-y+yc),white)

        # Checking and updating value of 
        # decision parameter based on algorithm 
        if d1 < 0:
            x +=1
            dx = dx + (2 * ry * ry) 
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1 
            y -= 1
            dx = dx + (2 * ry * ry) 
            dy = dy - (2 * rx * rx) 
            d1 = d1 + dx - dy + (ry * ry)
        pygame.display.flip()
  
    # Decision parameter of region 2 
    d2 = ((ry * ry) * ((x + 0.5) * (x + 0.5))) + ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry)
  
    # Plotting points of region 2 
    while (y >= 0):
  
        # Print points based on 4-way symmetry
        gfxdraw.pixel(screen,round(x+xc),round(y+yc),white)
        gfxdraw.pixel(screen,round(-x+xc),round(y+yc),white)
        gfxdraw.pixel(screen,round(x+xc),round(-y+yc),white)
        gfxdraw.pixel(screen,round(-x+xc),round(-y+yc),white)
        
        # Checking and updating parameter 
        # value based on algorithm 
        if d2 > 0:
            y -= 1
            dy = dy - (2 * rx * rx) 
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1 
            x += 1
            dx = dx + (2 * ry * ry) 
            dy = dy - (2 * rx * rx) 
            d2 = d2 + dx - dy + (rx * rx)
        pygame.display.flip()


midptellipse(10, 15, 50, 50)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()