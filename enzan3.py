# coding: utf-8

listA = [20,4,"plus"]
listB = [20,4,"minus"]
listC = [20,4,"devide"]
listD = [20,4,"multiply"]
listE = [20,4,"aiu"]

listF = listB

def fn(list):
    def sep():
        print "--------------------------------------"
    def pr(x):
        print x
    sep()


    if list[2] == "plus":
        result = listF[0]+listF[1]
        sep()
        pr(result)
        sep()
    elif list[2] == "minus":
        result = listF[0]-listF[1]
        sep()
        pr(result)
        sep()
    elif list[2] == "multiply":
        result = listF[0]*listF[1]
        sep()
        pr(result)
        sep()
    elif list[2] == "divide":
        result = listF[0]-listF[1]
        sep()
        pr(result)
        sep()
    else:
        sep()
        pr("Invalid input value.")
        sep()

fn(listF)

# 数値の受け渡し部分作成
# line_profilerのコードを解析して、ヒット回数を記録する部分を抽出