# coding: utf-8


print "--------------------------------------"

def judge(obj):
    """ 引数の型を判定する """
    if isinstance(obj, int):
        return 1
 
    if isinstance(obj, float):
        return 1
 
    if isinstance(obj, list):
        return 2
 
    if isinstance(obj, str):
        return 3
 
 
res1 = judge("aaa")
res2 = judge(1)
res3 = judge(1.1)
res4 = judge([1, 2, 3])

print (res1)
print (res2)
print (res3)
print (res4)