# coding: utf-8
from numpy import random

def inputPart():
    sampleList = [123,0,1293878392817873281234321234323454321234321234321869878879843828494,"あいう","adbhjdnh","A13BB32"]
    print (sampleList)
    print str(sampleList).decode("string-escape")
    choiceList = [random.choice(sampleList),random.choice(sampleList),random.choice(sampleList)]
    print (choiceList)



inputPart()