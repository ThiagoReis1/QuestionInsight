from math import *

#início e entrada de valores
pocoes = float (input())

raiz5 = sqrt(5)

#snowberry
snowberry = float (pocoes * ((raiz5 - 1) / 4))

#sais de fogo
fg = float (5 - (2 * raiz5))
sf = sqrt (fg)
saisfogo = float (pocoes * sf)

#amanita
amanita =  float (pocoes * (5 * (5 - (2 * raiz5))))

#saída
#print ("Precisamos da seguinte quantidade de snowberry (em gramas)")
print (round (snowberry, 2))
#print ("Precisamos da seguinte quantidade de sais de fogo (em gramas)")
print (round (saisfogo, 2))
#print ("Precisamos da seguinte quantidade de amanita (em gramas)")
print (round (amanita, 2))