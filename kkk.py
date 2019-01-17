import numpy as np
"""
x = np.arange(9).reshape(3, 3)
y = [
    [0,0,0],
    [1,1,1],
    [2,2,2]
    ]

pList = []
for i in y:
    pList.append(i[0])
    pList.append(i[1])
    pList.append(i[2])

print (x)


print "-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-"


print (x)
print "-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-"
print (y)
print (pList)
print(len(y))
"""


li=[1,2,3,4]
li2=[1,2,3]

lili = li + li2

"""
for x in li[:]:
    if x in li2: li.remove(x)
"""

def deliteDuplicates(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

