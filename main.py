import sys, pygame
import math
import condition
import copy
import calc
import board

#initialize the pygame
pygame.init()

#displayのサイズ設定
size = width, height = 800, 800
black = 0, 0, 0

#色


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

#font設定
texts = ["1VS1", "VSAI", "QUIT"]
font_size = math.floor(250/len(texts))
Zen_Kurenaido = pygame.font.SysFont('Zen_Kurenaido',font_size)

#0 = menu, 
scean = 0

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


#min,maxとりあえず再起で最終局面を最大化するように書こうと思うけど多分無理なので
#盤面の評価関数を作ろうと思う


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

def play_reverse():
    screen.fill(black)
    if turn == 0:
        initiate()
    if (pygame.mouse.get_pressed()[0]== True):
        set_list(calc.get_place(calc.get_mouse_coord()))
    #スクリーンの色(RGB)
    board.board()
    board.draw_piece(position)


#title
pygame.display.set_caption("オセロ")

#left,top,width,height
def is_inside(mouse_coord, list):
    if list[0] < mouse_coord[0] < list[0] + list[2] and list[1] < mouse_coord[1] < list[1] + list[3]:
        return True
    return False

def menu():
    #メニュー画面を作る
    #普通に1v1とvaiを作る
    
    global scean
    screen.fill(color[1]) 

    mouse = pygame.mouse.get_pos()
    box_list =  calc.for_rect_in_pygame(width, height, width/2, height * 0.2, height*0.05, len(texts))
    
    for i in range(0, len(texts)):
        pygame.draw.rect(screen, color[0],box_list[i])
        screen.blit(Zen_Kurenaido.render(texts[i], True, text_color[1]) , (calc.find_screen_mid(width, len(texts[i]) * font_size/2)[0], calc.find_menu_height(height, height*0.2, height*0.05, len(texts))[1][i]))
    for i in box_list:
        if is_inside(mouse, i):
            #マウスが置かれている状態での色かえ
            pygame.draw.rect(screen, color[2],i)
            for i in range(0, len(texts)):
                screen.blit(Zen_Kurenaido.render(texts[i], True, text_color[1]) , (calc.find_screen_mid(width, len(texts[i]) * font_size/2)[0], calc.find_menu_height(height, height*0.2, height*0.05, len(texts))[1][i]))
    if event.type == pygame.MOUSEBUTTONDOWN:
            if is_inside(mouse, box_list[0]):
                scean = 1
            if is_inside(mouse, box_list[1]):
                scean = 2
            if is_inside(mouse, box_list[2]):
                scean = 3

#gameループ
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    if scean == 0:
        menu()
    elif scean == 1:
        play_reverse()
            
    else:
        pass
    pygame.display.update()