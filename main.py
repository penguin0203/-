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

#ターン
turn = 0
#文字を入力できるようにするため
A,B,C,D,E,F,G,H = "A","B","C","D","E","F","G","H"

#開始盤面
#リストのリストで統一
initial_position = [[D,4,1],[E,4,0], [D,5,0],[E,5,1]]

#局面
position = []

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
#駒をひとつだけ描写する時はタプルの最後に,をつける
def draw_piece(v):
    for i in v:
        place = get_mid((i[0],i[1]))
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

#横にA~H縦に1~8
#A,8などを入力するとそれに対するますの横軸縦軸を返す
def get_coord(v):
    alpha_num = ord(v[0])-64
    return((alpha_num*board_width/7, v[1] * board_height/7), (alpha_num*(board_width/7) + board_width/7, v[1] * (board_height/7) + board_height/7))

#軸入力に対してA,8などを返す
def get_place(v):
    return [chr(math.floor(v[0]/(board_width/7)) +64), math.floor(v[1]/(board_height/7))]

#ますを入力するとその中心を返す,駒を置くため
def get_mid(v):
    ver = get_coord(v)[0]
    return((ver[0]+ board_height/14), (ver[1]+ board_width/14))

def board():
    #四角を表示
    pygame.draw.rect(screen, green, pygame.Rect(board_size,board_place))
    #top/leftからスタート
    pygame.draw.aaline(screen, black, top_dot[0], bottom_dot[0], True)
    draw_lines(black, screen, top_dot, bottom_dot)
    draw_lines(black, screen, left_dot, right_dot)

#マウスで触るとコーディネートをえる
def get_mouse_coord():
    x,y = pygame.mouse.get_pos()
    return [x, y]

#駒のリストを作りそれを保持する
#リストの中身を書く
#初めはinitialからスタートする
#ターンを作る
def set_list():
    global turn
    global position
    mouse_coord = get_place(get_mouse_coord())
    if (turn % 2 == 1):
        mouse_coord.append(0)
        position.append(mouse_coord)
    else:
        mouse_coord.append(1)
        position.append(mouse_coord)
    turn += 1
        
def initiate():
    global position
    position = initial_position

#制約
#一度置いたますの上にはおけないように
def place_check():
    pass
    

#title
pygame.display.set_caption("オセロ")

#gameループ
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    if turn == 0:
        initiate()
    if (pygame.mouse.get_pressed()[0]== True):
        set_list()
    
    #スクリーンの色(RGB)
    board()
    draw_piece(position)
    draw_piece(((B, 8, 1),))
    pygame.display.update()