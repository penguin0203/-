#オセロのボードに関する関数
import calc
import pygame
import numpy as np

size = width, height = 800, 800

black = 0, 0, 0
green = 0,255,0

board_size = board_left, board_top=width*0.1,height*0.1
board_place = board_right, board_bottom=width*0.8, height*0.8
board_width = board_right-board_left
board_height = board_bottom-board_top

#白
head = 1
#黒
tail = 0

screen = pygame.display.set_mode(size)


#縦線
top_dot = [(i, width * 0.1) for i in np.arange(board_left+board_width/7, board_right + board_width/7, board_width/7)]
bottom_dot = [(i, height * 0.9) for i in np.arange(board_left + board_width/7, board_right+ board_width/7, board_width/7)]

#横線
left_dot = [(width * 0.1, i) for i in np.arange(board_top+board_height/7, board_bottom + board_height/7, board_height/7)]
right_dot = [(height * 0.9, i) for i in np.arange(board_top + board_height/7, board_bottom+ board_height/7, board_height/7)]

#駒を作る
#場所を受けてその位置を中心に駒を置く
#listのpygameを受ける
#side, headかtailか
#駒をひとつだけ描写する時はタプルの最後に,をつける
def draw_piece(v):
    for i in v:
        place = calc.get_mid((i[0],i[1]))
        #ボードがいに描写しないように
        if (board_top < place[1] and place[1] < (board_top+board_bottom)):
            if (board_left < place[0] and place[0] < (board_right+board_left)):
                #表、白
                if (i[2] == head):
                    pygame.draw.circle(screen, (255,255,255), (place[0], place[1]), ((board_width/16)))
                #裏、黒
                if (i[2] == tail):
                    pygame.draw.circle(screen, black, (place[0],place[1]), ((board_width/16)))
            
def draw_lines(color, place, v1,v2):
    for i in range(0, len(v1)):
        pygame.draw.aaline(place, color,v1[i], v2[i])



def board():
    #四角を表示
    pygame.draw.rect(screen, green, pygame.Rect(board_size,board_place))
    #top/leftからスタート
    pygame.draw.aaline(screen, black, top_dot[0], bottom_dot[0], True)
    draw_lines(black, screen, top_dot, bottom_dot)
    draw_lines(black, screen, left_dot, right_dot)