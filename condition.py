import copy

#制約
#一度置いたますの上にはおけないように
#falseおけないTrueおける
def place_check(mouse_coord, position):
    for place in position:
        if place[0] == mouse_coord[0] and place[1] == mouse_coord[1]:
            return False
    return True

#ひっくり返す条件
#一定のinputに対してもし、縦、横、斜めで相手の駒がありそれを自分の駒で挟んでいた時相手の駒をひっくり返す。
#縦横斜めを相手の駒があるかぎり+,-して自分の駒があればそれをリストにして返す
#listを見て縦、横、斜めで相手の駒がある時自分の駒がくるまでリストの番号をとってくる
#方法１
#周りの駒を全てとってくるその内違うコマだけをリストに加えるを繰り返す
#方法2
#先に縦、横、斜めを全てとるその中から可能な列に絞る
#縦,同じ記号A,Bなどの列を全てとる、端にいくまで
#横,同じ数字の列を全てとる、端にいくまで
#斜め,文字+1,数値+1,+,-に関しては全ての組み合わせで文字or数値が端にいくまで
#とってきた番号の駒の0,1を変える,ひとつでもひっくり返した数を返す


def reverse_list(input, list):
    place = copy.copy(input)
    rev_place = copy.copy(input)
    #1なら0,0なら1に変換
    rev_place[2] =(rev_place[2]+1) %2
    tmp = []
    output_list = []
    #横に対して#プラスに対して
    #右
    #次のますを作る,それがあるかないかを判定する
    while True:
        #文字をひとつ進める
        place[0] = chr(ord(place[0]) + 1)
        rev_place[0] = chr(ord(rev_place[0]) + 1)
        if place[0] == "I":
            break
        if rev_place in list:
            tmp.append(copy.copy(rev_place))
        elif place in list:
            output_list.extend(copy.copy(tmp))
            break
        else:
            break
    #位置の初期化
    tmp = []
    #左
    place = copy.copy(input)
    rev_place = copy.copy(place)
    rev_place[2] =(place[2]+1) %2
    while True:
        #文字をひとつ進める
        place[0] = chr(ord(place[0]) - 1)
        rev_place[0] = chr(ord(rev_place[0]) - 1)
        if place[0] == "@":
            break
        if rev_place in list:
            tmp.append(copy.copy(rev_place))
        elif place in list:
            output_list.extend(copy.copy(tmp))
            break
        else:
            break
    tmp = []
    #下
    place = copy.copy(input)
    rev_place = copy.copy(place)
    rev_place[2] =(place[2]+1) %2
    while True:
        #数字
        place[1] = (place[1] + 1)
        rev_place[1] = (rev_place[1] + 1)
        if place[1] == 9:
            break
        if rev_place in list:
            tmp.append(copy.copy(rev_place))
        elif place in list:
            output_list.extend(copy.copy(tmp))
            break
        else:
            break
    tmp = []
    #上
    place = copy.copy(input)
    rev_place = copy.copy(place)
    rev_place[2] =(place[2]+1) %2
    while True:
        #数字
        place[1] = (place[1] - 1)
        rev_place[1] = (rev_place[1] - 1)
        if place[1] == 0:
            break
        if rev_place in list:
            tmp.append(copy.copy(rev_place))
        elif place in list:
            output_list.extend(copy.copy(tmp))
            break
        else:
            break
    tmp = []
    #斜め
    #右下
    place = copy.copy(input)
    rev_place = copy.copy(place)
    rev_place[2] =(place[2]+1) %2
    while True:
        #数字
        place[0], place[1] = chr(ord(place[0]) + 1), place[1] + 1
        rev_place[0], rev_place[1] = chr(ord(rev_place[0]) + 1), rev_place[1] + 1
        if place[0] == "I" or place[0] == 9:
            break
        if rev_place in list:
            tmp.append(copy.copy(rev_place))
        elif place in list:
            output_list.extend(copy.copy(tmp))
            break
        else:
            break
    
    tmp = []
    place = copy.copy(input)
    rev_place = copy.copy(place)
    rev_place[2] =(place[2]+1) %2
    #斜め
    #右上
    while True:
        #数字
        place[0], place[1] = chr(ord(place[0]) + 1), place[1] - 1
        rev_place[0], rev_place[1] = chr(ord(rev_place[0]) + 1), rev_place[1] - 1
        if place[0] == "I" or place[0] == 1:
            break
        if rev_place in list:
            tmp.append(copy.copy(rev_place))
        elif place in list:
            output_list.extend(copy.copy(tmp))
            break
        else:
            break
        
    tmp = []
    place = copy.copy(input)
    rev_place = copy.copy(place)
    rev_place[2] =(place[2]+1) %2
    #斜め
    #左上
    while True:
        #数字
        place[0], place[1] = chr(ord(place[0]) - 1), place[1] - 1
        rev_place[0], rev_place[1] = chr(ord(rev_place[0]) - 1), rev_place[1] - 1
        if place[0] == "@" or place[0] == 1:
            break
        if rev_place in list:
            tmp.append(copy.copy(rev_place))
        elif place in list:
            output_list.extend(copy.copy(tmp))
            break
        else:
            break
    tmp = []
    place = copy.copy(input)
    rev_place = copy.copy(place)
    rev_place[2] =(place[2]+1) %2
    #斜め
    #左下
    while True:
        #数字
        place[0], place[1] = chr(ord(place[0]) - 1), place[1] + 1
        rev_place[0], rev_place[1] = chr(ord(rev_place[0]) - 1), rev_place[1] + 1
        if place[0] == "@" or place[0] == 9:
            break
        if rev_place in list:
            tmp.append(copy.copy(rev_place))
        elif place in list:
            output_list.extend(copy.copy(tmp))
            break
        else:
            break
    print(output_list)
    return (output_list)


