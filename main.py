import sys, pygame
import numpy
import math
#initialize the pygame
pygame.init()

#displayのサイズ設定
size = width, height = 800, 800
black = 0, 0, 0
green = 0,255,0
head = 1
tail = 0
#文字を入力できるようにするため
A,B,C,D,E,F,G,H = "A","B","C","D","E","F","G","H"

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

#縦線
top_dot = [(i, width * 0.1) for i in numpy.arange(board_left+board_width/7, board_right + board_width/7, board_width/7)]
bottom_dot = [(i, height * 0.9) for i in numpy.arange(board_left + board_width/7, board_right+ board_width/7, board_width/7)]

#横線
left_dot = [(width * 0.1, i) for i in numpy.arange(board_top+board_height/7, board_bottom + board_height/7, board_height/7)]
right_dot = [(height * 0.9, i) for i in numpy.arange(board_top + board_height/7, board_bottom+ board_height/7, board_height/7)]



#駒を作る
#場所を受けてその位置を中心に駒を置く
#listのpygameを受ける
#side, headかtailか
def draw_piece(place, side):
    #表、白
    if (side == head):
        pygame.draw.circle(screen, (255,255,255), place, ((board_width/16)))
    #裏、黒
    if (side == tail):
        pygame.draw.circle(screen, black, place, ((board_width/16)))
        
def draw_lines(color, place, v1,v2):
    for i in range(0, len(v1)):
        pygame.draw.aaline(place, color,v1[i], v2[i])

#横にA~H縦に1~8
#A,8などを入力するとそれに対するますの横軸縦軸を返す
def get_coord(alpha, num):
    alpha_num = ord(alpha)-64
    return((alpha_num*board_width/7, num * board_height/7), (alpha_num*(board_width/7) + board_width/7, num * (board_height/7) + board_height/7))

#軸入力に対してA,8などを返す
def get_place(*v):
    return(math.floor(v[0]/(board_height/7)), chr(math.floor(v[1]/(board_height/7)) +64))

#ますを入力するとその中心を返す,駒を置くため
def get_mid(*v):
    ver, hori = get_coord(v[0], v[1])
    return((ver[0]+ board_height/14), (ver[1]+ board_width/14))

def board():
    #四角を表示
    pygame.draw.rect(screen, green, pygame.Rect(board_size,board_place))
    #top/leftからスタート
    pygame.draw.aaline(screen, black, top_dot[0], bottom_dot[0], True)
    draw_lines(black, screen, top_dot, bottom_dot)
    draw_lines(black, screen, left_dot, right_dot)
    

#title
pygame.display.set_caption("オセロ")

#gameループ
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    
    #スクリーンの色(RGB)
    board()
    draw_piece(get_mid(B, 8), 1)
    pygame.display.update()