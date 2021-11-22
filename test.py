import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    
def back(a,b,c):
    if a == 0 and b == 0 and c == 0:
            print("end")
            return 0
    if a != 0:
            print(a)
            return back(a - 1,b,c)
    if b != 0:
            print(b)
            return back(a,b - 1,c)
    if c != 0:
        print(c)
        return back(a,b,c - 1)