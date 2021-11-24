import sys, pygame
import numpy
import math
import condition
import copy
import numpy as np
#initialize the pygame
pygame.init()

#displayのサイズ設定
size = width, height = 800, 800
black = 0, 0, 0
green = 0,255,0

#色
#白
head = 1
#黒
tail = 0

#とってきた色たち
color = [(245,245,198), (125,168,123),(50,103,101),(39,37,61),]
text_color = [(33,33,33),(117,117,117),(189,189,189),(0,0,0)]

#ターン
turn = 0
#文字を入力できるようにするため
A,B,C,D,E,F,G,H = "A","B","C","D","E","F","G","H"

#開始盤面
#リストのリストで統一
initial_position = [[D,4,1],[E,4,0], [D,5,0],[E,5,1]]

#開始の設定が完了したかどうか
initiate_flag = False



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


#メニューの設定
#AIと戦う
#1V1をする
#やめる
#スクリーンの中心に長さの中心を合わせる
def find_screen_mid(screen_length, length):
    return (screen_length/2) - (length/2), (screen_length/2) + (length/2)

#横の高さを求める
def find_menu_height(screen_height, margin_height, padding_height, menu_num):
    menu_height = (screen_height - (margin_height * 2 + padding_height * (menu_num +1))) / menu_num
    start_output_list = [i for i in np.arange(margin_height+padding_height, screen_height -  margin_height, padding_height+menu_height)]
    end_output_list = list(map(lambda num: num + menu_height, start_output_list))
    output_list = [[start_output_list[i], end_output_list[i]] for i in range(len(start_output_list))]
    return output_list, start_output_list, menu_height

#pygame用の長さに合わせる
#left,top,width,height
def for_rect_in_pygame(screen_length, screen_height, length, margin_height, padding_height, menu_num):
    left = find_screen_mid(screen_length, length)[0]
    width = length
    top = find_menu_height(screen_height, margin_height, padding_height, menu_num)[1]
    height = find_menu_height(screen_height, margin_height, padding_height, menu_num)[2]
    output = [[left, i, width, height] for i in top]
    return (output)




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
def set_list(input):
    global turn
    global position
    end_flag = False
    mouse_coord = input
    #白と黒をターンによって追加
    mouse_coord.append(turn%2)
    if len(possible_hands(position, turn)) == 0:
        print("pass")
        end_flag = True
        turn += 1
    #おけるかどうかを確認
    if mouse_coord in possible_hands(position, turn):
        end_flag = False
        position.append(mouse_coord)
        convert(condition.reverse_list(mouse_coord, position))
        turn += 1
    if end_flag == True:
        print("end")
        print(piece_count(position))

#駒の数を数える
#白,黒
def piece_count(list):
    return sum([i[2] == 1 for i in list]), len(list) - sum([i[2] == 1 for i in list])

#リストで完全一致を探してそれの末尾を1なら0に0なら１に変換する
def convert(changing_list):
    for i in position:
        if i in changing_list:
            i[2] = (i[2] + 1) %2
    
#開始局面
def initiate():
    global position
    global initiate_flag
    if initiate_flag == False:
        position = copy.copy(initial_position)
        initiate_flag = True

#勝敗判定
#パス判定
#周りの駒を全て調べて着手できなかった場合 or 全ての空いているますを調べて着手できなかった場合
#全てのますに対して
def possible_hands(position, turn):
    possible_position = []
    #駒が置かれていなくてかつreverse_listのlenが1以上のもの場所
    for i in range(ord(A), ord("I")):
        for j in range(1, 9):
            if condition.place_check((chr(i), j), position) == True and len(condition.reverse_list([chr(i), j, turn%2], position)) != 0:
                possible_position.append([chr(i), j, turn%2])
    return possible_position

#font設定
texts = ["1 VS 1", "VS AI", "QUIT"]
font_size = math.floor(250/len(texts))
Zen_Kurenaido = pygame.font.SysFont('Zen_Kurenaido',font_size)


def play_reverse():
    if turn == 0:
        initiate()
    if (pygame.mouse.get_pressed()[0]== True):
        set_list(get_place(get_mouse_coord()))
    #スクリーンの色(RGB)
    board()
    draw_piece(position)


#title
pygame.display.set_caption("オセロ")

#left,top,width,height
def is_inside(mouse_coord, list):
    if list[0] < mouse_coord[0] < list[0] + list[2] and list[1] < mouse_coord[1] < list[1] + list[3]:
        return True
    return False


    

#gameループ
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    #メニュー画面を作る
    #普通に1v1とvaiを作る
    screen.fill(color[1])

    mouse = pygame.mouse.get_pos()
    box_list =  for_rect_in_pygame(width, height, width/2, height * 0.2, height*0.05, len(texts))
    
    for i in range(0, len(texts)):
        pygame.draw.rect(screen, color[0],box_list[i])
        screen.blit(Zen_Kurenaido.render(texts[i], True, text_color[1]) , (find_screen_mid(width, len(texts[i]) * font_size/2)[0], find_menu_height(height, height*0.2, height*0.05, len(texts))[1][i]))
    for i in box_list:
        if is_inside(mouse, i):
            #マウスが置かれている状態での色かえ
            pygame.draw.rect(screen, color[2],i)
            for i in range(0, len(texts)):
                screen.blit(Zen_Kurenaido.render(texts[i], True, text_color[1]) , (find_screen_mid(width, len(texts[i]) * font_size/2)[0], find_menu_height(height, height*0.2, height*0.05, len(texts))[1][i]))
        
    
    
    
    pygame.display.update()