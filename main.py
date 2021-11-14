import sys, pygame
#initialize the pygame
pygame.init()

#displayのサイズ設定
size = width, height = 1000, 1000
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#ボード
board_size = board_x, board_y = 800, 800

def board():
    #スクリーンに描写
    screen.blit()

#title
pygame.display.set_caption("オセロ")

#gameループ
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    #スクリーンの色(RGB)
    screen.fill((black))
    pygame.display.update()