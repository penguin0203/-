import sys, pygame
import numpy
#initialize the pygame
pygame.init()

#displayのサイズ設定
size = width, height = 800, 800
black = 0, 0, 0
green = 0,255,0

screen = pygame.display.set_mode(size)

#x,y表示に変換
#return x,y,floot
def to_x_y(left, top):
    return(left - width/2, top-height/2)

#return left, width,floot
def to_pygame(x, y):
    return(x+width/2, y+height/2)
    
#ボード
board_size = board_left, board_top=width*0.1,height*0.1
board_place = board_right, board_bottom=width*0.8, height*0.8
board_width = board_right-board_left
board_height = board_bottom-board_top

top_dot = [(board_top, i) for i in numpy.arange(board_left+board_width/8, board_right, board_width/8)]
bottom_dot = [(board_bottom, i) for i in numpy.arange(board_left + width/8, board_right, board_width/8)]



def draw_lines(color, place, v1,v2):
    for i in range(v1):
        pygame.draw.aaline(place, color,v1[i], v2[i])


def board():
    #四角を表示
    pygame.draw.rect(screen, green, pygame.Rect(board_size,board_place))
    #top/leftからスタート
    pygame.draw.aaline(screen, black, [100,162.5], [100,225.0], True)
    

#title
pygame.display.set_caption("オセロ")

#gameループ
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    
    #スクリーンの色(RGB
    board()
    pygame.display.update()