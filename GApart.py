# coding: utf-8
import random
import sys
sys.setrecursionlimit(10000)


"""
GAの内容
評価関数を設け、選択、交叉、突然変異させる

まず、Calc()関数を実行したファズに含まれる要素の評価値をあげる
calc()の中でも、実行した数が少ない部分を実行したファズに含まれる要素の評価値をあげる
ファズリストの中で、選択頻度が少ない要素の評価値をあげる（ここ微妙）

選択
評価値の高い要素を高確率で選択するリストを作成する・・・1

交叉
単純に、calc()を実行したファズ同士で要素の入れ替えをする・・・2

突然変異
評価値が低い要素からランダムでリストに入れる


2つの方法で試す。

1つ目の手順（ファズ単位でのGA）
calc()関数を実行したファズを選択。
選択したファズの要素同士だけで交叉する。
突然変異で、選択したファズに含まれていない要素を入れる。

2つ目の手順（要素単位でのGA)
calc()関数を実行したファズの要素の評価値をあげる
選ばれた回数が少ない要素の評価値をあげる
上記２つで選ばれた要素に重み付けし、選択確率を与える。
選択確率をもとに、要素を選択してファズを生成する
生成したファズ同士を交叉したファズを作成する
一部のファズの要素を、選ばれていない要素と入れ替える（突然変異）

"""

def sep():
    print "-/-/-/-/-/-/-/-/-/-/-/-"


#二次元のリストにも対応した重複削除関数
def deliteDuplicates(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

#最初のファズの要素リスト
original = [
    1,
    234,
    543,
    766,
    44,
    5,
    100,
    20,
    111,
    371,
    0,
    26182576726545671723454736273454323454327667827345432763478372,
    0.134,
    "あいう",
    "saerf",
    "plus",
    "AAAd123482934",
    "minus",
    "devide",
    "multiply",
    "divide",
    "plas",
    "minos",
    "multipy"
    ]

#calc()を実行したファズリスト
element = [
    [371, 543, 'あいう'],
    [234, 543, 'plas'],
    [44, 766, 'AAAd123482934'],
    [371, 100, 'あいう'],
    [100, 0, 'devide'],
    [234, 111, 'minos'],
    [100, 371, 'devide'],
    [0.134, 100, 'multiply'],
    [543, 44, 'devide'],
    [111, 371, 'AAAd123482934'],
    [371, 371, 'plas'],
    [766, 20, 'saerf'],
    [234, 44, 'AAAd123482934'],
    [0.134, 0, 'plus'],
    [543, 0, 'minos'],
    [1, 234, 'divide'],
    [5, 234, 'plas'],
    [371, 371, 'devide'],
    [5, 20, 'minos'],
    [543, 0.134, 'divide'],
    [20, 766, 'divide'],
    [1, 1, 'AAAd123482934'],
    [543, 111, 'minos'],
    [543, 234, 'multipy']
    ]

length = len(element)
flatten = []
for i in element:
    flatten.append(i[0])
    flatten.append(i[1])
    flatten.append(i[2])

#elementを1次元に変換したリスト
flatten = list(set(flatten))

#交叉部分
def cross(list1,list2):
    prov1 = [list1[0],list2[1],list1[2]]
    prov2 = [list2[0],list1[1],list2[2]]

    prov3 = [list1[0],list1[1],list2[2]]
    prov4 = [list2[0],list2[1],list1[2]]

    prov5 = [list2[0],list1[1],list1[2]]
    prov6 = [list1[0],list2[1],list2[2]]

    return prov1,prov2,prov3,prov4,prov5,prov6

#突然変異部分
def mutation(parent):
    copy = original
    for x in copy[:]:
        if x in flatten:
            copy.remove(x)
    
    insert = random.choice(original)
    kid1 = [insert,parent[1],parent[2]]
    kid2 = [parent[0],insert,parent[2]]
    kid3 = [parent[0],parent[1],insert]

    return kid1,kid2,kid3

def GAmain():
    crossOutput = []
    mutationOutput = []

    for crossover in range(100):
        chosen = random.sample(element,2)
        resCross = cross(chosen[0],chosen[1])
        crossOutput.extend(resCross)

    for mutate in range(50):
        chosen = random.choice(element)
        resMutation = mutation(chosen)
        mutationOutput.extend(resMutation)
    
    union = crossOutput + mutationOutput
    union2 = deliteDuplicates(union)
    uniLen = len(union2)
    
    #子ファズが300に満たない場合は300になるまで突然変異でファズを追加
    while uniLen<300:
        chosen = random.choice(element)
        resMutation = mutation(chosen)
        mutationOutput.extend(resMutation)
        uniLen = len(union2)
    
    fuzzkids = random.sample(union2,300)
    return fuzzkids

kids = GAmain()


def judge(obj):
    """ 入力値の型を判定する """
    if isinstance(obj, int):
        return 1

    if isinstance(obj, float):
        return 1

    if isinstance(obj, list):
        return 2

    if isinstance(obj, str):
        return 3

def calc(list):

    if list[2] == "plus":
        result = list[0]+list[1]
    elif list[2] == "minus":
        result = list[0]-list[1]
    elif list[2] == "multiply":
        result = list[0]*list[1]
    elif list[2] == "divide":
        if list[1] == 0:
            result = "Do not divide by 0."
        else:
            result = list[0]/list[1]      
    else:
        result = "Operator is invalid."
    return result

def main():
    for i in kids:
        judgeValue0 = judge(i[0])
        judgeValue1 = judge(i[1])
        judgeValue2 = judge(i[2])
        
        if judgeValue0 == 1 and judgeValue1 == 1 and judgeValue2 == 3:
            output = calc(i)

        else:
            output = "error"
        
        #print str(i).decode("string-escape")
        sep()

main()