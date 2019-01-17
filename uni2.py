# coding: utf-8
import random
"""
inputPart 入力値生成
judge 入力値の型を判定
calc 計算部分
main 以上の関数を動かす
以上4つの関数で構成
"""

@profile
def fn():
    def inputPart():

        elements = [
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
        length = len(elements)-1
        extraction = [
            elements[random.randint(0,length)],
            elements[random.randint(0,length)],
            elements[random.randint(0,length)]
            ]
        return extraction


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
        def sep():
            print "--------------------------------------"
        def pr(x):
            print x
        sep()

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
        inputValue = inputPart()
        judgeValue0 = judge(inputValue[0])
        judgeValue1 = judge(inputValue[1])
        judgeValue2 = judge(inputValue[2])
        if judgeValue0 == 1 and judgeValue1 == 1 and judgeValue2 == 3:
            output = calc(inputValue)
        else:
            output = "error"
        
        print "----------------------------------------------------------------------"
        print(output)
        print str(inputValue).decode("string-escape")
    """
        print "- ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ "
        print "test part"
        print "------------------------------"
        print "入力したリストの値"
        print str(inputValue).decode("string-escape")    
        print "------------------------------"
        print "入力値1つめの判定"
        print (judgeValue0)
        print "------------------------------"
        print "入力値2つめの判定"
        print (judgeValue1)    
        print "------------------------------"
        print "入力値3つめの判定"
        print (judgeValue2)
        print "------------------------------"
        print "出力の値"
        print (output)
    """
    main()

fn()

