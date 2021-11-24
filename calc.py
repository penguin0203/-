#計算用のfunction
import pygame 
import math
import numpy as np


size = width, height = 800, 800


board_size = board_left, board_top=width*0.1,height*0.1
board_place = board_right, board_bottom=width*0.8, height*0.8
board_width = board_right-board_left
board_height = board_bottom-board_top

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

#マウスで触るとコーディネートをえる
def get_mouse_coord():
    x,y = pygame.mouse.get_pos()
    return [x, y]
