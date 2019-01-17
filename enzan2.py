
def fn():
    def sep():
        print "--------------------------------------"
    def pr(x):
        print x
    sep()
    A = input("Please input A:" )
    B = input("Please input B:" )
    ope = raw_input("Please input operator(plus, minus, multiply or divide can be enterd)  operator:" )
    if ope == "plus":
        result = A+B
        sep()
        pr(result)
        sep()
    elif ope == "minus":
        result = A-B
        sep()
        pr(result)
        sep()
    elif ope == "multiply":
        result = A*B
        sep()
        pr(result)
        sep()
    elif ope == "divide":
        result = A/B
        sep()
        pr(result)
        sep()
    else:
        sep()
        pr("Invalid input value.")
        sep()
fn()


# 数値の受け渡し部分作成
# line_profilerのコードを解析して、ヒット回数を記録する部分を抽出