# coding: utf-8

# 区切り線の関数
def sep():
    print "--------------------------------------"

# プリントを短くする関数
def pr(x):
    print x

# 計算部分
def calc():
    sep()
    # 数値A・数値B・演算子の入力
    A = input("Please input A:" )
    B = input("Please input B:" )
    ope = raw_input("Please input operator(plus, minus, multiply or divide can be enterd)  operator:" )

    if 

    # 演算子ごとにif分岐
    if ope == "plus":
        result = A+B

    elif ope == "minus":
        result = A-B

    elif ope == "multiply":
        result = A*B

    elif ope == "divide":
        result = A/B

    else:
        result = "Invalid input value."
    
    sep()
    print(result)
    sep()

calc()